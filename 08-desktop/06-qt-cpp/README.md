# Qt 6 C++ Todo List Desktop Application

A cross-platform native desktop application built with **Qt 6**, **C++17**, and the **MVVM / Model-View** architectural pattern.

## 🚀 Overview

This submodule demonstrates native desktop app development using Qt 6. It showcases custom QAbstractListModel implementations, QSS theme switching, JSON serialization, and unit testing with Qt Test.

## ✨ Features

- 💻 **Native Cross-Platform Desktop UI**: Runs natively on Windows, macOS, and Linux.
- 🏗️ **MVVM Architecture**: Clean separation between `TodoItem` (Model), `TodoModel` (ViewModel), and `MainWindow` (View).
- 🌓 **Theme Support**: Built-in Light and Dark QSS stylesheets.
- 💾 **Data Persistence & Export**: Saves to local JSON and supports sample data import.
- 🧪 **Unit Tests**: Full model coverage using Qt Test Framework.

## 🛠️ Tech Stack

- **C++17**
- **Qt 6.x** (Core, GUI, Widgets, Test)
- **CMake** / **qmake** build systems

## 📁 Project Structure

```
06-qt-cpp/
├── CMakeLists.txt
├── todo-list.pro
├── main.cpp
├── src/
│   ├── MainWindow.cpp / .h
│   ├── StorageManager.cpp / .h
│   ├── TodoItem.cpp / .h
│   └── TodoModel.cpp / .h
├── docs/
│   ├── ARCHITECTURE.md
│   ├── BUILD_GUIDE.md
│   └── QT_CONCEPTS.md
├── resources/
└── tests/
```

## ⚙️ Build & Run

### Prerequisites

- Qt 6.5+ SDK installed
- CMake 3.16+ or qmake
- C++17 compatible compiler (GCC, Clang, or MSVC)

### Build with CMake

```bash
mkdir build && cd build
cmake ..
cmake --build .
```

For more detailed build instructions and troubleshooting, see [BUILD_GUIDE.md](docs/BUILD_GUIDE.md) and [ARCHITECTURE.md](docs/ARCHITECTURE.md).
