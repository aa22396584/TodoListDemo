# Bevy Engine Todo List (Rust)

A data-driven Todo List application built with the **Bevy Engine** (Rust) using the **Entity Component System (ECS)** architecture.

## 🚀 Overview

This submodule demonstrates state management and GUI construction using the Rust Bevy game engine. It showcases ECS design patterns (Entities, Components, Systems, Resources, Events) and local file storage in Rust.

## ✨ Features

- 🦀 **Pure Rust & Bevy ECS**: Decoupled architecture using systems, resources, and custom events.
- 🎨 **Bevy UI Nodes**: Dynamic UI layout using Flexbox via Bevy's native UI hierarchy.
- 🔄 **Event-Driven**: Decoupled event streams (`TodoCreatedEvent`, `TodoToggledEvent`, etc.).
- 💾 **File Persistence**: Automatic JSON storage serialization in Rust.
- 🌐 **WASM Compatible**: Compilable to WebAssembly for browser deployment.

## 🛠️ Tech Stack

- **Rust (2021 Edition)**
- **Bevy Engine 0.12+**
- **Serde / Serde JSON**

## 📁 Project Structure

```
05-bevy/
├── Cargo.toml
├── clippy.toml
├── src/
│   ├── main.rs
│   ├── components/
│   ├── events/
│   ├── plugins/
│   ├── resources/
│   ├── systems/
│   └── utils/
└── docs/
    ├── ARCHITECTURE.md
    └── ECS_GUIDE.md
```

## ⚙️ Building & Running

### Prerequisites

- Rust 1.75+ toolchain (`rustup`)

### Execution

```bash
# Navigate to submodule
cd 09-game-engines/05-bevy

# Run native desktop app
cargo run --release
```

### Running Tests

```bash
cargo test
```

For more guidance on Bevy ECS architecture and WASM build details, see [ECS_GUIDE.md](docs/ECS_GUIDE.md) and [ARCHITECTURE.md](docs/ARCHITECTURE.md).
