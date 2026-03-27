# Common Engineering Plugin

A foundational plugin for Claude Code containing essential agents and skills for software engineers. This plugin provides common development utilities, diagram generation, documentation helpers, and other engineering tools to streamline your development workflow.

## Prerequisites

**Important**: This plugin requires the `shared-mcp` plugin to be installed first. The shared-mcp plugin provides the Exa MCP server used for web research and code context lookups.

```bash
# Install shared-mcp first
/plugin install shared-mcp@my-claude-code-marketplace

# Then install common-engineering
/plugin install common-engineering@my-claude-code-marketplace
```

## Overview

The `common-engineering` plugin is designed as an extensible toolkit for software engineers, providing frequently-used capabilities as reusable agents and skills. Currently focused on professional diagram generation, this plugin will expand to include more engineering tools over time.

## Features

### Mermaid Diagram Generation

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

### Web Research Specialist

Expert internet researcher for comprehensive topic research across ANY subject - technical debugging, news, business information, or general knowledge.

**Research Capabilities:**
- **Technical Debugging**: Find solutions to library errors, framework issues, and code problems
- **Code Research**: API documentation, SDK usage, and implementation examples
- **Company/Business Research**: Company information, industry analysis, business insights
- **News & Current Events**: Recent articles, breaking news, time-based research
- **General Research**: Any topic requiring web investigation

**Key Features:**
- ✅ **Comprehensive scope**: Handles technical, business, news, and general research
- ✅ **Smart tool selection**: Automatically uses best research tool (Exa, Tavily, or WebSearch)
- ✅ **Company research**: Exa's company_research for business information and LinkedIn data
- ✅ **News optimization**: Tavily with time-based filtering for current events
- ✅ **Code-optimized**: Leverages Exa's `get_code_context_exa` for programming research
- ✅ **Delegates to librarian**: Automatically routes official documentation requests to librarian agent
- ✅ **Structured output**: Executive summary, detailed findings, sources, and recommendations

### Librarian Agent

Library documentation specialist for fetching official API docs, code examples, and library references.

**Dual-Mode Operation:**
- **Documentation Lookup**: When you mention a library ("How do I use React hooks?", "Supabase auth")
- **Proactive Research**: Suggests libraries for your development tasks ("I need to add file uploads")

**Supported Libraries:**
- 50,000+ libraries with version-specific documentation
- JavaScript/TypeScript: React, Vue, Next.js, Node.js, Express
- Python: Django, FastAPI, SQLAlchemy, Celery
- Go, Rust, Java, Ruby, PHP, and many more

**Key Features:**
- ✅ **Official docs only**: Version-specific API documentation from official sources
- ✅ **Topic-focused search**: Retrieve docs for specific topics (authentication, routing, etc.)
- ✅ **Code examples**: Real code snippets from official documentation
- ✅ **Proactive suggestions**: Recommends libraries based on your development needs
- ✅ **Seamless fallback**: Delegates to web-research-specialist if Context7 is unavailable

**Distinction from web-research-specialist:**
- `librarian`: Official documentation via Context7 (docs, APIs, examples)
- `web-research-specialist`: Web search for debugging, community solutions, forums

### Technical Documentation Writer

Professional technical documentation creation with interactive guided templates.

**Supported Document Types:**
- **One-Pager**: Concise proposals for features, changes, or decisions (1-3 pages)
- **RFC**: Request for Comments - detailed design proposals for cross-team review
- **TSD**: Technical Specification Documents (APIs, data models, interfaces)
- **ADR**: Architecture Decision Records (technology choices, trade-offs)
- **POC/Experiment**: Proof of concepts and technical experiments

**Key Capabilities:**
- ✅ **Interactive guided creation**: Step-by-step prompts help you articulate your ideas
- ✅ **Template-based structure**: Professional formats for one-pagers, proposals, and feature briefs
- ✅ **Research integration**: Seamlessly gather context via web-research-specialist agent
- ✅ **Diagram generation**: Optional Mermaid diagrams via mermaid skill
- ✅ **Multiple output formats**: Export to Word, PDF, or Markdown

**Adaptive Workflow**: The agent adapts to your preparation level - whether you have everything ready, just the basics, or are starting from an idea.

### Project Management Plan

Generate professional Excel project management plans with full-year Gantt charts.

**Supported Tabs:**
- **Main Program Plan**: Task list with 52-week Monday-based Gantt chart
- **Charters**: Team roles and PICs tracking
- **Budget**: Cost tracking by category
- **RAID Logs**: Risks, Assumptions, Issues, and Dependencies

**Key Capabilities:**
- ✅ **Full-year timeline**: Jan-Dec with every Monday as a column header
- ✅ **Auto year detection**: From project start_date, task dates, or current year
- ✅ **Dynamic Gantt bars**: Conditional formatting based on task dates
- ✅ **Status validation**: Dropdown with standard statuses (Not Started, In Progress, Completed, Blocked, On Hold)
- ✅ **Template rows**: 30 rows ready for task entry

### Code Review

Structured code review for git branch changes with findings classified by severity and dimension.

**Review Dimensions:**
- **Correctness**: Logic errors, edge cases, race conditions, error handling, test coverage
- **Security**: Input validation, auth checks, credential exposure, cryptographic issues
- **Maintainability**: Complexity, naming, duplication, code organization
- **Scalability**: N+1 queries, unbounded operations, resource leaks, missing pagination

**Key Capabilities:**
- ✅ **Automatic diff analysis**: Detects base branch and generates structured review from git diff
- ✅ **Noise pre-filtering**: Skips lockfiles, generated code, binaries, vendor directories
- ✅ **Severity classification**: Critical, Major, Minor, Nit — with clear action required for each
- ✅ **Confidence filter**: Only flags issues with realistic harm scenarios — no speculative noise
- ✅ **Positive observations**: Reinforces good practices alongside issue identification
- ✅ **Verdict**: Ready to merge / Merge after fixes / Needs significant rework
- ✅ **Zero dependencies**: No MCP servers, API keys, or external tools required

### Future Additions

This plugin will be expanded with additional engineering tools including:
- Common development workflows
- And more...

## Installation

### Prerequisites

#### Required for Mermaid Diagrams: Mermaid CLI
The diagram generation feature requires `mermaid-cli` to be installed globally:

```bash
npm install -g @mermaid-js/mermaid-cli
```

**Verify installation:**
```bash
mmdc --version
```

You should see output like: `10.6.1` or similar.

#### Required for Web Research: shared-mcp Plugin

The web research specialist uses Exa's powerful search capabilities from the `shared-mcp` plugin. Make sure you have:

1. **Installed the shared-mcp plugin**:
   ```bash
   /plugin install shared-mcp@my-claude-code-marketplace
   ```

2. **Configured the EXA_API_KEY** as described in the [shared-mcp README](../shared-mcp/README.md)

**Note**: Without the `EXA_API_KEY` configured in shared-mcp, the web research specialist will fall back to using Claude's built-in WebSearch tool, which is less optimized for code research.

#### Optional for Librarian: Context7 API Key

The librarian agent uses the Context7 MCP server to fetch official library documentation. The free tier works without an API key, but you can optionally get one for higher rate limits.

**Optional - Get API Key at:** https://context7.com/dashboard

**Add to your shell config (~/.zshrc or ~/.bashrc):**
```bash
# Optional: Context7 API key for librarian agent (free tier works without key)
export CONTEXT7_API_KEY="your-api-key-here"
```

**Reload your shell:**
```bash
source ~/.zshrc  # or source ~/.bashrc
```

**Note**: The librarian agent works with the free tier without an API key. Setting the key is optional for increased rate limits.

#### Optional for Technical Documentation: document-skills Plugin

The techdocs-writer agent can export documents to Word (.docx) or PDF formats using the `document-skills` plugin (Anthropic's official document manipulation plugin). This is optional - you can still create and export markdown documents without it.

**To enable Word/PDF export:**
```bash
/plugin install document-skills
```

**Note**: Markdown output works without document-skills. The plugin is only needed for .docx and .pdf formats.

#### Required for Project Management Plan: openpyxl

The `/project-management-plan` skill generates Excel workbooks and requires the openpyxl Python library.

**Install openpyxl:**
```bash
pip install openpyxl
```

**Verify installation:**
```bash
python3 -c "import openpyxl; print(openpyxl.__version__)"
```

### Install the Plugin

1. **Add this marketplace to Claude Code** (if not already added):
   ```bash
   /plugin marketplace add https://github.com/irfansofyana/my-claude-code-marketplace
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

### Web Research Specialist Agent

The `web-research-specialist` agent is automatically invoked when you need to research technical problems, business information, current events, or gather information from multiple online sources.

**Example requests:**
```
# Technical debugging
"I'm getting a 'Module not found' error with webpack 5, can you research solutions?"
"Research the best practices for implementing infinite scrolling with React"

# Business/Company research
"Tell me about Anthropic as a company"
"What's the latest news about Tesla?"
"Find information about Stripe's business model"

# News & Current Events
"What's the latest news about AI regulation?"
"What are the recent developments in quantum computing?"

# General research
"Compare state management solutions for Vue.js - Pinia vs Vuex"
"Find examples of how to configure Next.js partial prerendering"
```

**Agent behavior:**
- For **code/API research**: Uses Exa's `get_code_context_exa` for highest quality results
- For **company/business research**: Uses Exa's `company_research_exa` for comprehensive business information
- For **news/current events**: Uses Tavily with time-based filtering for recent articles
- For **official documentation**: Automatically delegates to librarian agent
- Falls back to alternative tools if primary tool fails

**Output format**: The agent provides structured findings with:
1. Executive Summary (2-3 sentence overview)
2. Detailed Findings (organized by relevance)
3. Sources and References (direct links)
4. Recommendations (best approaches)
5. Additional Notes (caveats, warnings)

### TechDocs Writer Agent

The `techdocs-writer` agent is automatically invoked when you request technical documentation. It guides you through creating professional documents using interactive prompts.

**Example requests:**
```
"Create a one-pager for migrating to OAuth 2.0"
"Write a proposal for implementing dark mode"
"Help me document a decision about database selection"
"Create a one-pager proposing a new feature"
```

**How it works:**
- The agent adapts to your preparation level (whether you have all details ready or just an idea)
- Provides interactive prompts to gather information section-by-section
- Offers research assistance via web-research-specialist when needed
- Can generate diagrams via mermaid skill if requested
- Exports to Word, PDF, or Markdown format

**Output formats:**
- Markdown (default, no additional plugins required)
- Word (.docx) via document-skills plugin
- PDF via document-skills plugin

### Librarian Agent

The `librarian` agent is automatically invoked when you ask about library documentation or mention specific libraries/frameworks.

**Example requests:**
```
"How do I use React hooks for state management?"
"What's the Supabase authentication API for JavaScript?"
"I need to add file uploads to my Express app - what library should I use?"
"Show me the Django ORM documentation for filtering queries"
```

**How it works:**
- **Documentation Lookup**: Automatically detects library names and fetches official docs
- **Proactive Mode**: Suggests relevant libraries when you describe development tasks
- **Topic-Focused**: Narrows docs to specific topics (auth, routing, database, etc.)
- **Fallback**: If Context7 is unavailable, delegates to web-research-specialist

**Direct invocation:**
```
"Use the librarian agent to find React Context API docs"
```

### Project Management Plan Skill

The `/project-management-plan` skill generates a complete Excel project management plan with Gantt chart, team charters, budget tracking, and RAID logs.

**Example request:**
```
"Generate a project management plan for a platform modernization project"
```

**How it works:**
- Interactive guided workflow gathers project details
- Generates Excel workbook with 4 tabs: Main Program Plan, Charters, Budget, RAID Logs
- Full-year Gantt chart with Monday-based weekly columns
- Auto-detects year from project dates or uses current year

**Requirements:**
- Python 3 with openpyxl (`pip install openpyxl`)

### Code Review Skill

The code review skill is automatically invoked when you ask to review code changes on your current branch.

**Example requests:**
```
"Review my code changes against main"
"Do a code review of this branch"
"Check my diff before I open a PR"
"Review my changes focusing on security"
```

**How it works:**
- Detects the base branch automatically (defaults to `main`/`master`)
- Generates a diff and pre-filters noise (lockfiles, generated code, binaries)
- Reads full file context for each changed file
- Analyzes against four dimensions: correctness, security, maintainability, scalability
- Produces a structured report with severity-classified findings and a merge verdict

**Requirements:**
- Git (for diff generation)
- No additional dependencies

### Direct Agent Invocation

You can also explicitly request agents in your prompts:

```
"Use the mermaid-expert agent to create a sequence diagram for..."
"Use the web-research-specialist agent to find solutions for..."
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
- **shared-mcp plugin**: Provides Exa/Tavily MCP servers for web research
- **Context7 MCP**: Built into common-engineering for librarian agent (free tier works without API key)
- **document-skills plugin**: Optional - for Word/PDF export in techdocs-writer (Markdown works without it)
- **openpyxl**: Python library for `/project-management-plan` Excel generation (`pip install openpyxl`)
- **/tmp directory**: Used for validation temporary files

### Installation Verification

Test that everything is working:

```bash
# 1. Check mermaid-cli installation
mmdc --version

# 2. Check Exa API key is set (configured via shared-mcp plugin)
echo $EXA_API_KEY

# 3. Test the Mermaid agent by asking Claude:
"Create a simple flowchart with Start and End nodes"

# 4. Test the Web Research agent by asking Claude:
"Research how to implement dark mode in React"

# 5. Test the Librarian agent by asking Claude:
"How do I use Supabase authentication in JavaScript?"

# 6. Test the Project Management Plan skill by asking Claude:
"Generate a project management plan for a website redesign project"
```

If Claude successfully generates diagrams, performs research, and creates project plans, your setup is complete!

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

#### 5. Web research specialist not using Exa tools

**Problem:** Agent falls back to WebSearch instead of using Exa.

**Solution:**
```bash
# 1. Ensure shared-mcp plugin is installed
/plugin install shared-mcp@my-claude-code-marketplace

# 2. Check if EXA_API_KEY is set
echo $EXA_API_KEY

# 3. If not set, see shared-mcp README for configuration
# Restart Claude Code after setting the environment variable
```

#### 6. Exa API errors

**Problem:** "Invalid API key" or Exa-related errors.

**Solution:**
- Verify your API key is correct: https://exa.ai
- Check your API usage limits haven't been exceeded
- Ensure the key is properly set in your environment (no extra quotes or spaces)

### Getting Help

If you encounter issues:
1. **For Mermaid issues**:
   - Check that `mmdc --version` works in your terminal
   - Verify you can run: `echo 'graph TD; A-->B' | mmdc -i - -o /tmp/test.svg`
   - Review the skill documentation in `plugins/common-engineering/skills/mermaid/`
2. **For Web Research issues**:
   - Verify `EXA_API_KEY` is set: `echo $EXA_API_KEY`
   - Check your Exa account status at https://exa.ai
   - Try explicitly requesting code research: "Use get_code_context_exa to find..."
3. **General plugin issues**:
   - Check Claude Code plugin status: `/plugin`
   - Reload the plugin to pick up changes
   - Review agent logs if available

## Development

### Plugin Structure

```
plugins/common-engineering/
├── .claude-plugin/
│   └── plugin.json                     # Plugin metadata + MCP config
├── agents/
│   ├── mermaid-expert.md               # Mermaid diagram specialist
│   ├── techdocs-writer.md              # Technical documentation specialist
│   ├── web-research-specialist.md      # Web research specialist
│   └── librarian.md                    # Library documentation specialist
├── skills/
│   ├── .claude/
│   │   └── settings.local.json         # Permissions configuration
│   ├── mermaid/
│   │   ├── SKILL.md                    # Main skill definition
│   │   ├── flowchart-diagram-reference.md
│   │   ├── sequence-diagrams-reference.md
│   │   └── architecture-diagram-reference.md
│   ├── code-review/
│   │   ├── SKILL.md                    # Skill definition + output format + example
│   │   └── references/
│   │       ├── REFERENCE.md            # Index of reference files
│   │       └── review-checklist.md     # Review criteria per dimension
│   └── techdocs/
│       ├── SKILL.md                    # Main skill definition
│       ├── writing-guidelines.md       # Technical writing best practices
│       ├── question-bank.md            # Reusable question patterns
│       └── templates/one-pager/
│           ├── template.md             # Document structure
│           ├── guidance.md             # Section-by-section guidance
│           ├── quality-checklist.md    # Validation criteria
│           └── examples.md             # Completed examples
└── README.md                           # This file
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

Completed features:
- [x] Mermaid diagram generation with validation
- [x] Web research specialist agent
- [x] Technical documentation writer (v1.1.0)
- [x] Librarian agent for library docs (v1.6.0)
- [x] Enhanced web-research-specialist with general research, company research, and news capabilities (v1.7.0)
- [x] Project Management Plan skill with full-year Gantt charts (v1.10.0)

Planned additions to this plugin:
- [x] Code review agent
- [ ] Shell script expert agent

## Author

**irfansofyana**

## License

This plugin is part of the Claude Code Marketplace.

## Learn More

- [Mermaid Documentation](https://mermaid.js.org/)
- [Claude Code Plugin Development](https://docs.claude.com/en/docs/claude-code)
- [Iconify Icon Search](https://iconify.design/) (for architecture diagrams)
