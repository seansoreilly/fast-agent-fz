# Resource Loading Options for Fat Zebra Agent

This document outlines several approaches to improve how documentation and other resources are loaded into the Fat Zebra AI agent using the Fast Agent MCP framework.

## 1. Batch Loading

Load multiple files at once in batches to reduce the number of API calls:

```python
# Load all documentation files in batches
doc_files = glob.glob(os.path.join(doc_path, "**/*.md"), recursive=True)
batch_size = 5  # Adjust based on file sizes

for i in range(0, len(doc_files), batch_size):
    batch = doc_files[i:i+batch_size]
    batch_content = {}

    for file_path in batch:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                file_name = os.path.basename(file_path)
                batch_content[file_name] = f.read()
        except Exception as e:
            logger.error(f"Failed to load {file_path}: {str(e)}")

    # Load batch as a single resource
    await agent.with_resource(
        f"Documentation batch {i//batch_size + 1}",
        batch_content,
        "fatzebra"
    )
```

## 2. Resource Collections

Use the ResourceCollection feature to organize and load related documents:

```python
from mcp_agent.resources import ResourceCollection

# Create a resource collection
docs = ResourceCollection("fat_zebra_docs")

# Add all markdown files to collection
for md_file in markdown_files:
    try:
        with open(md_file, 'r', encoding='utf-8') as f:
            file_name = os.path.basename(md_file)
            docs.add(file_name, f.read())
    except Exception as e:
        logger.error(f"Failed to load {md_file}: {str(e)}")

# Load the entire collection at once
await agent.with_resources(docs, "fatzebra")
```

## 3. Dedicated Documentation Server

Create a separate MCP server specifically for handling documentation:

```yaml
# In fastagent.config.yaml:
servers:
  fatzebra_docs:
    command: "uv"
    args: ["run", "docs_server.py"]
    working_dir: "servers"
```

```python
# Then in your agent definition:
@fast.agent(
    instruction="Assist with any queries regarding the Fat Zebra API",
    servers=["fatzebra", "fatzebra_docs", "brave_search_api"],
    use_history=True
)
```

## 4. Document Embeddings

Pre-process and embed documents for more efficient retrieval:

```python
# Create a vector database from documentation
from mcp_agent.embedding import create_embeddings

# Initialize during agent setup
embeddings_db = create_embeddings(markdown_files)

# Register with agent
agent.register_knowledge_base(embeddings_db)
```

## 5. MCP Prompt Templates

Use MCP prompt templates for loading documentation:

```python
# Define a prompt template for loading documentation
await agent.apply_prompt("load_documentation", {
    "files": markdown_files,
    "base_path": doc_path
})
```

Each approach has different advantages depending on the number of files, their size, and how they'll be used in conversation. The best solution may involve combining several of these approaches.
