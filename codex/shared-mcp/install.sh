#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'EOF'
Install the shared-mcp MCP servers into Codex config.toml.

Usage:
  install.sh [--global]
  install.sh --project [path]

Options:
  --global        Install into ~/.codex/config.toml (default)
  --project PATH  Install into PATH/.codex/config.toml
  -h, --help      Show this help
EOF
}

scope="global"
project_root=""

while [[ $# -gt 0 ]]; do
  case "$1" in
    --global)
      scope="global"
      shift
      ;;
    --project)
      scope="project"
      if [[ $# -gt 1 ]] && [[ ! "$2" =~ ^-- ]]; then
        project_root="$2"
        shift 2
      else
        project_root="$PWD"
        shift
      fi
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      echo "Unknown argument: $1" >&2
      usage >&2
      exit 1
      ;;
  esac
done

script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
template_path="${script_dir}/config.toml"

if [[ ! -f "${template_path}" ]]; then
  echo "Template not found: ${template_path}" >&2
  exit 1
fi

if ! command -v codex >/dev/null 2>&1; then
  echo "codex CLI not found in PATH" >&2
  exit 1
fi

if ! command -v npx >/dev/null 2>&1; then
  echo "npx not found in PATH" >&2
  exit 1
fi

if [[ "${scope}" == "global" ]]; then
  target_config="${HOME}/.codex/config.toml"
else
  target_config="${project_root}/.codex/config.toml"
fi

target_dir="$(dirname "${target_config}")"
mkdir -p "${target_dir}"

tmp_file="$(mktemp)"
cleanup() {
  rm -f "${tmp_file}"
}
trap cleanup EXIT

if [[ -f "${target_config}" ]]; then
  awk '
    BEGIN {skip=0}
    /^# BEGIN shared-mcp codex$/ {skip=1; next}
    /^# END shared-mcp codex$/ {skip=0; next}
    skip == 0 {print}
  ' "${target_config}" > "${tmp_file}"
else
  : > "${tmp_file}"
fi

if [[ -s "${tmp_file}" ]] && [[ "$(tail -c 1 "${tmp_file}" 2>/dev/null || true)" != $'\n' ]]; then
  printf '\n' >> "${tmp_file}"
fi

cat "${template_path}" >> "${tmp_file}"
mv "${tmp_file}" "${target_config}"

echo "Installed shared-mcp Codex config into ${target_config}"
echo "Configured MCP servers:"
echo "  - shared_mcp_tavily"
echo "  - shared_mcp_exa"
echo "  - shared_mcp_brave_search"
echo
echo "Next steps:"
echo "  1. Ensure TAVILY_API_KEY, EXA_API_KEY, and BRAVE_API_KEY are exported in your shell."
echo "  2. Run: codex mcp list"
echo "  3. Restart Codex CLI/IDE if it was already open."
