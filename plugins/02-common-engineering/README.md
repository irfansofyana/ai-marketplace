# Common Engineering Plugin

A foundational plugin for Claude Code containing essential agents and skills for software engineers. This plugin provides common development utilities, diagram generation, documentation helpers, and other engineering tools to streamline your development workflow.

## Overview

The `common-engineering` plugin is designed as an extensible toolkit for software engineers, providing frequently-used capabilities as reusable agents and skills. Currently focused on professional diagram generation, this plugin will expand to include more engineering tools over time.

## Features

### Mermaid Diagram Generation (Available Now)

Professional Mermaid diagram creation with automatic validation and self-healing capabilities.

**Supported Diagram Types:**
- **Sequence Diagrams**: API flows, authentication sequences, microservices communication
- **Architecture Diagrams**: Cloud infrastructure, CI/CD pipelines, service relationships
- **Flowchart Diagrams**: Process flows, decision trees, algorithm logic

**Key Capabilities:**
- ✅ **Zero-error diagrams**: All diagrams validated before delivery using `mermaid-cli`
- ✅ **Self-healing**: Automatically fixes common syntax errors
- ✅ **Comprehensive syntax**: Full Mermaid feature set support
- ✅ **200,000+ icons**: Support for iconify.design icons in architecture diagrams
- ✅ **Professional quality**: Built-in size guidelines and best practices

### Future Additions

This plugin will be expanded with additional engineering tools including:
- Code documentation generators
- API documentation helpers
- Architecture decision records (ADR) templates
- Common development workflows
- And more...

## Installation

### Prerequisites

#### Required: Mermaid CLI
The diagram generation feature requires `mermaid-cli` to be installed globally:

```bash
npm install -g @mermaid-js/mermaid-cli
```

**Verify installation:**
```bash
mmdc --version
```

You should see output like: `10.6.1` or similar.

### Install the Plugin

1. **Add this marketplace to Claude Code** (if not already added):
   ```bash
   /plugin marketplace add /Users/irfanputra/Personal/my-claude-code-marketplace
   ```

2. **Install the plugin:**
   ```bash
   /plugin install common-engineering@my-claude-code-marketplace
   ```

## Usage

### Mermaid Expert Agent

The `mermaid-expert` agent is automatically available to Claude Code. Simply ask Claude to create diagrams, and it will invoke the agent when appropriate.

**Example requests:**
```
"Create a sequence diagram showing the OAuth authentication flow"
"Generate an architecture diagram for a microservices setup with API Gateway, Auth Service, and User Service"
"Draw a flowchart for the user registration process"
```

### Direct Agent Invocation

You can also explicitly request the mermaid-expert agent in your prompts:

```
"Use the mermaid-expert agent to create a sequence diagram for..."
```

## Diagram Examples

### Sequence Diagram
**Use for:** API interactions, authentication flows, service communication

**Example request:**
```
"Create a sequence diagram showing how a user logs in with JWT authentication"
```

**Generated output:** A validated Mermaid sequence diagram showing the login flow between Client, API Server, and Auth Service.

### Architecture Diagram
**Use for:** System architecture, cloud infrastructure, service relationships

**Example request:**
```
"Create an architecture diagram for a typical 3-tier web application with load balancer, web servers, and database"
```

**Generated output:** A validated Mermaid architecture diagram with groups, services, and connections.

### Flowchart Diagram
**Use for:** Process flows, decision trees, algorithm logic

**Example request:**
```
"Create a flowchart showing the order processing workflow with payment validation"
```

**Generated output:** A validated Mermaid flowchart with decision nodes, process steps, and flow connections.

## How It Works

### Validation Workflow

Every diagram goes through a rigorous validation process:

1. **Generate**: Claude creates the Mermaid diagram syntax
2. **Validate**: The diagram is tested using `mermaid-cli` (`mmdc` command)
3. **Self-heal**: If validation fails, common syntax errors are automatically fixed:
   - Hyphens in labels → Replaced with underscores
   - Reserved words in identifiers → Prefixed with safe characters
   - Quote mismatches → Corrected
4. **Confirm**: Only validated diagrams are delivered to you
5. **Output**: You receive working Mermaid code ready to use

### Quality Guarantees

- **No broken diagrams**: 100% of delivered diagrams are pre-validated
- **Syntax correctness**: All diagrams tested with actual Mermaid renderer
- **Best practices**: Follows Mermaid conventions and size guidelines
- **Error transparency**: If validation fails, you'll see the error and fix attempt

## Dependencies

### System Requirements
- **Node.js**: Required for `mermaid-cli` (npm package)
- **mermaid-cli**: The Mermaid command-line renderer
- **/tmp directory**: Used for validation temporary files

### Installation Verification

Test that everything is working:

```bash
# 1. Check mermaid-cli installation
mmdc --version

# 2. Test the plugin by asking Claude:
"Create a simple flowchart with Start and End nodes"
```

If Claude successfully generates and validates a diagram, your setup is complete!

## Troubleshooting

### Common Issues

#### 1. `mmdc: command not found`

**Problem:** `mermaid-cli` is not installed or not in PATH.

**Solution:**
```bash
# Install globally
npm install -g @mermaid-js/mermaid-cli

# Verify installation
which mmdc
mmdc --version
```

#### 2. `Permission denied` when running mmdc

**Problem:** Insufficient permissions for npm global packages.

**Solution:**
```bash
# Option 1: Use sudo (macOS/Linux)
sudo npm install -g @mermaid-js/mermaid-cli

# Option 2: Configure npm to use user directory
mkdir ~/.npm-global
npm config set prefix '~/.npm-global'
echo 'export PATH=~/.npm-global/bin:$PATH' >> ~/.bashrc
source ~/.bashrc
npm install -g @mermaid-js/mermaid-cli
```

#### 3. Validation fails repeatedly

**Problem:** Complex diagram syntax or edge cases.

**Solution:**
- Check the error message from `mmdc` command
- Simplify the diagram request
- Refer to the reference documentation in `skills/mermaid/` for syntax guidelines

#### 4. Diagrams render but look incorrect

**Problem:** Syntax is valid but diagram doesn't match expectations.

**Solution:**
- Review the generated Mermaid code
- Provide more specific requirements in your request
- Reference the Mermaid documentation: https://mermaid.js.org/

### Getting Help

If you encounter issues:
1. Check that `mmdc --version` works in your terminal
2. Verify you can run: `echo 'graph TD; A-->B' | mmdc -i - -o /tmp/test.svg`
3. Check Claude Code plugin status: `/plugin`
4. Review the skill documentation in `plugins/02-common-engineering/skills/mermaid/`

## Development

### Plugin Structure

```
plugins/02-common-engineering/
├── .claude-plugin/
│   └── plugin.json              # Plugin metadata
├── agents/
│   └── mermaid-expert.md        # Mermaid diagram specialist agent
├── skills/
│   ├── .claude/
│   │   └── settings.local.json  # Permissions configuration
│   └── mermaid/
│       ├── SKILL.md             # Main skill definition
│       ├── flowchart-diagram-reference.md
│       ├── sequence-diagrams-reference.md
│       └── architecture-diagram-reference.md
└── README.md                    # This file
```

### Adding New Features

To contribute new engineering tools to this plugin:

1. **For new agents**: Add agent definition to `agents/` directory
2. **For new skills**: Create skill directory under `skills/` with `SKILL.md`
3. **Update plugin version**: Increment version in `.claude-plugin/plugin.json`
4. **Document the feature**: Update this README with the new capability
5. **Test locally**:
   ```bash
   /plugin uninstall common-engineering@my-claude-code-marketplace
   /plugin install common-engineering@my-claude-code-marketplace
   ```

### Reference Documentation

Comprehensive syntax guides are available in the `skills/mermaid/` directory:
- `flowchart-diagram-reference.md` (879 lines): Complete flowchart syntax
- `sequence-diagrams-reference.md` (797 lines): Complete sequence diagram syntax
- `architecture-diagram-reference.md` (175 lines): Architecture diagram syntax

## Roadmap

Planned additions to this plugin:
- [ ] Web research specialist agent
- [ ] Code review agent
- [ ] Shell script expert agent
- [ ] Documentation specialist agent

## Author

**irfansofyana**

## License

This plugin is part of the Claude Code Marketplace.

## Learn More

- [Mermaid Documentation](https://mermaid.js.org/)
- [Claude Code Plugin Development](https://docs.claude.com/en/docs/claude-code)
- [Iconify Icon Search](https://iconify.design/) (for architecture diagrams)
