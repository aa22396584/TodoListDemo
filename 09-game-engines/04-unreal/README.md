# Unreal Engine 5 Todo List

A 3D game engine Todo List application built with **Unreal Engine 5**, **C++**, and **UMG UI Designer**.

## 🚀 Overview

This submodule demonstrates building non-game utility user interfaces inside Unreal Engine 5. It features a hybrid C++ backend with Blueprint UMG widgets for UI rendering, and uses Unreal's `USaveGame` system for data persistence.

## ✨ Features

- 🎮 **3D Game Engine UI**: Implemented in Unreal Motion Graphics (UMG).
- ⚡ **C++ Core Logic**: `UTodoManager` handles data structures and business operations.
- 💾 **SaveGame System**: Serializes todo items directly into `.sav` format.
- 🎨 **Modular Blueprint Widgets**: Separated into reusable widget classes.

## 🛠️ Tech Stack

- **Unreal Engine 5.x**
- **C++20**
- **UMG (Unreal Motion Graphics)**

## 📁 Project Structure

```
04-unreal/
├── TodoListUE.uproject
├── Source/
│   └── TodoListUE/
│       ├── TodoItem.h
│       ├── TodoManager.h / .cpp
│       ├── TodoSaveGame.h / .cpp
│       └── TodoWidgetBase.h / .cpp
├── Content/
│   ├── Blueprints/
│   └── UI/
└── docs/
    ├── ARCHITECTURE.md
    └── SETUP_GUIDE.md
```

## ⚙️ How to Run

### Prerequisites

- Unreal Engine 5.1+
- Visual Studio 2022 (with Game Development with C++) or Xcode (on macOS)

### Opening the Project

1. Right-click `TodoListUE.uproject` and select **Generate Visual Studio project files**.
2. Open `TodoListUE.sln` and compile the source.
3. Open `TodoListUE.uproject` in Unreal Editor and press **Play (PIE)**.

For complete documentation, refer to [SETUP_GUIDE.md](docs/SETUP_GUIDE.md) and [ARCHITECTURE.md](docs/ARCHITECTURE.md).
