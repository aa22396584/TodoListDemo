# Vue 3 Todo List App

A modern, responsive Todo List application built with **Vue 3**, **Composition API** (`<script setup>`), and **Vite**.

## 🚀 Overview

This submodule demonstrates the core principles of Vue 3 development using the Composition API, single-file components (SFC), reactivity (`ref`, `watch`), and local storage persistence.

## ✨ Features

- 📝 **Create Todo**: Fast entry with validation and trim formatting.
- 🔘 **Toggle Completion**: Seamless reactive status updates.
- 🗑️ **Delete Todo**: Remove single or clear completed items.
- 💾 **LocalStorage Sync**: Automatic persistence on every change.
- 🎨 **Modern Responsive UI**: Styled with clean CSS and transition effects.

## 🛠️ Technology Stack

- **Vue 3.x**: Composition API with `<script setup>`
- **Vite**: Ultra-fast frontend build tool and dev server
- **JavaScript (ESNext)**: Standard JavaScript syntax
- **LocalStorage API**: Web browser storage

## 📁 Project Structure

```
03-vue3/
├── index.html
├── package.json
├── vite.config.js
└── src/
    ├── App.vue
    ├── main.js
    ├── style.css
    └── components/
        ├── TodoInput.vue
        ├── TodoItem.vue
        └── TodoList.vue
```

## ⚙️ Getting Started

### Prerequisites

- Node.js >= 18.0.0
- npm >= 9.0.0

### Installation

```bash
# Navigate to submodule directory
cd 03-modern-frameworks/03-vue3

# Install dependencies
npm install
```

### Development Server

```bash
npm run dev
```

Open your browser at `http://localhost:5173`.

### Production Build

```bash
npm run build
```

The output will be placed in the `dist` directory.
