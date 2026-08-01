# AppKit macOS Native Todo List App

A native macOS desktop application built with **Swift 5**, **AppKit**, and **Cocoa Design Patterns**.

## 🚀 Overview

This submodule demonstrates native macOS development using Apple's AppKit framework. It features traditional Cocoa architecture (MVC/MVVM), NSTableView integration, custom Touch Bar support, and native menu bar integration.

## ✨ Features

- 🍎 **Native macOS UI**: Native controls, Dark Mode support, and macOS design aesthetics.
- ⌨️ **Touch Bar Support**: Quick actions via MacBook Touch Bar integration.
- 📊 **NSTableView Data Source**: Efficient list rendering and cell reuse.
- 💾 **Storage Service**: Local data persistence with JSON encoder/decoder.
- ⚙️ **Preferences Window**: Customizable user settings.

## 🛠️ Tech Stack

- **Swift 5**
- **AppKit / Cocoa**
- **Xcode Project & XCTest**

## 📁 Project Structure

```
09-appkit-macos/
├── TodoListMac.xcodeproj
├── TodoListMac/
│   ├── AppDelegate.swift
│   ├── MainWindowController.swift
│   ├── Models/
│   ├── ViewControllers/
│   ├── Views/
│   └── Services/
├── TodoListMacTests/
└── docs/
    ├── APPKIT_GUIDE.md
    └── ARCHITECTURE.md
```

## ⚙️ Building & Running

### Prerequisites

- macOS 13.0+
- Xcode 14.0+

### Building via Xcode

1. Open `TodoListMac.xcodeproj` in Xcode.
2. Select the `TodoListMac` target and destination `My Mac`.
3. Press `Cmd + R` to build and run.

For deeper architectural details, see [APPKIT_GUIDE.md](docs/APPKIT_GUIDE.md) and [ARCHITECTURE.md](docs/ARCHITECTURE.md).
