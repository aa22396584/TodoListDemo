# Electron Vue Todo

一个使用 Electron 28+ 和 Vue 3 构建的现代化、功能丰富的桌面待办事项应用。

![Electron](https://img.shields.io/badge/Electron-28+-9feaf9?logo=electron&logoColor=white)
![Vue](https://img.shields.io/badge/Vue-3.4+-4FC08D?logo=vue.js&logoColor=white)
![TypeScript](https://img.shields.io/badge/TypeScript-5.4+-3178C6?logo=typescript&logoColor=white)
![Vite](https://img.shields.io/badge/Vite-5+-646CFF?logo=vite&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)

## 目录

- [项目简介](#项目简介)
- [核心特性](#核心特性)
- [技术栈](#技术栈)
- [Electron + Vue 整合说明](#electron--vue-整合说明)
- [与 Electron + React 的对比](#与-electron--react-的对比)
- [项目结构](#项目结构)
- [快速开始](#快速开始)
- [开发指南](#开发指南)
- [IPC 通信模式](#ipc-通信模式)
- [安全最佳实践](#安全最佳实践)
- [Vite + Electron 配置](#vite--electron-配置)
- [打包发布](#打包发布)
- [性能优化](#性能优化)
- [故障排除](#故障排除)
- [最佳实践](#最佳实践)
- [进阶主题](#进阶主题)
- [常见问题](#常见问题)
- [贡献指南](#贡献指南)

## 项目简介

Electron Vue Todo 是一个展示如何结合 Electron 和 Vue 3 构建跨平台桌面应用的完整示例。它不仅是一个功能完整的待办事项管理工具，更是学习 Electron + Vue 开发的最佳实践参考。

### 为什么选择 Electron + Vue？

1. **Vue 的优势**
   - 渐进式框架，学习曲线平缓
   - 优秀的响应式系统
   - 强大的 Composition API
   - 更小的包体积
   - 出色的中文文档

2. **与 React 相比的优势**
   - 模板语法更接近 HTML，更直观
   - 双向绑定减少样板代码
   - 内置指令系统（v-if, v-for 等）
   - 更好的性能（虚拟 DOM 优化）
   - 单文件组件（SFC）开发体验更好

3. **Electron 的跨平台能力**
   - 一次编写，处处运行
   - 访问原生 API
   - 强大的生态系统
   - 活跃的社区支持

## 核心特性

### 基础功能

- ✅ **待办事项管理**
  - 添加、编辑、删除待办事项
  - 标记完成/未完成
  - 双击编辑功能
  - 字符计数（最多 200 字符）

- 🔍 **智能过滤**
  - 查看全部待办
  - 仅显示活动项
  - 仅显示已完成项
  - 实时统计数据

- 💾 **数据持久化**
  - 自动保存到本地文件系统
  - JSON 格式存储
  - 支持数据导入/导出
  - 数据备份与恢复

### Electron 特性

- 🖥️ **原生桌面体验**
  - 自定义应用菜单
  - 系统托盘集成
  - 原生通知
  - 键盘快捷键（Cmd/Ctrl+N, Cmd/Ctrl+Q）

- 🔒 **安全性**
  - contextBridge 安全通信
  - 禁用 Node 集成
  - 启用上下文隔离
  - 内容安全策略（CSP）

- 📦 **跨平台打包**
  - Windows（NSIS 安装程序、便携版、ZIP）
  - macOS（DMG、ZIP，支持 x64 和 ARM64）
  - Linux（AppImage、DEB、RPM、TAR.GZ）

### Vue 3 特性

- ⚡ **Composition API**
  - 更好的代码组织
  - 逻辑复用性强
  - TypeScript 支持优秀
  - 更灵活的状态管理

- 🎨 **响应式设计**
  - 自适应布局
  - 移动端友好
  - 优雅的动画过渡
  - 现代化 UI/UX

- 🔄 **高性能渲染**
  - 虚拟 DOM 优化
  - 列表动画
  - 懒加载组件
  - 智能批量更新

## 技术栈

### 核心技术

| 技术 | 版本 | 说明 |
|------|------|------|
| Electron | 28+ | 桌面应用框架 |
| Vue | 3.4+ | 渐进式前端框架 |
| TypeScript | 5.4+ | 类型安全 |
| Vite | 5+ | 构建工具 |

### 开发依赖

```json
{
  "electron": "^28.2.3",           // Electron 框架
  "vue": "^3.4.21",                // Vue 3 框架
  "typescript": "^5.4.2",          // TypeScript 编译器
  "vite": "^5.1.5",                // Vite 构建工具
  "electron-builder": "^24.13.3",  // 打包工具
  "vite-plugin-electron": "^0.28.4", // Vite Electron 插件
  "@vitejs/plugin-vue": "^5.0.4",  // Vue 插件
  "vue-tsc": "^2.0.6"              // Vue TypeScript 检查
}
```

## Electron + Vue 整合说明

### 架构概述

Electron + Vue 应用由三个主要部分组成：

```
┌─────────────────────────────────────────┐
│           Electron 主进程               │
│  (electron/main.ts - Node.js 环境)     │
│                                         │
│  - 窗口管理                             │
│  - 文件系统操作                         │
│  - 系统菜单/托盘                        │
│  - IPC 通信处理                         │
└──────────────┬──────────────────────────┘
               │ IPC 通信
               ├─────────────────────┐
               │                     │
┌──────────────▼──────┐   ┌─────────▼──────────┐
│   Preload 脚本      │   │   渲染进程          │
│ (preload.ts)        │   │  (Vue 3 应用)       │
│                     │   │                     │
│ - contextBridge     │   │  - 用户界面         │
│ - 安全 API 暴露     │   │  - 组件系统         │
│                     │   │  - 状态管理         │
└─────────────────────┘   └─────────────────────┘
```

### 1. 主进程（Main Process）

主进程是应用的入口点，运行在 Node.js 环境中，负责：

```typescript
// electron/main.ts
import { app, BrowserWindow, ipcMain } from 'electron';

// 创建窗口
function createWindow() {
  const mainWindow = new BrowserWindow({
    width: 1000,
    height: 700,
    webPreferences: {
      preload: path.join(__dirname, 'preload.js'),
      contextIsolation: true,    // 启用上下文隔离
      nodeIntegration: false,     // 禁用 Node 集成
      sandbox: false,
    },
  });

  // 加载 Vue 应用
  if (isDevelopment) {
    mainWindow.loadURL('http://localhost:5173'); // Vite 开发服务器
  } else {
    mainWindow.loadFile('dist/index.html'); // 生产构建
  }
}

// IPC 处理器
ipcMain.handle('get-todos', async () => {
  return await loadTodosFromFile();
});

app.whenReady().then(createWindow);
```

**主要职责：**
- 创建和管理 BrowserWindow
- 处理应用生命周期事件
- 提供 IPC 通信接口
- 执行文件系统操作
- 创建原生菜单和托盘

### 2. Preload 脚本

Preload 脚本在渲染进程加载前运行，作为主进程和渲染进程之间的桥梁：

```typescript
// electron/preload.ts
import { contextBridge, ipcRenderer } from 'electron';

// 定义安全的 API
const electronAPI = {
  getTodos: () => ipcRenderer.invoke('get-todos'),
  addTodo: (text: string) => ipcRenderer.invoke('add-todo', text),
  // ... 更多 API
};

// 通过 contextBridge 暴露 API
contextBridge.exposeInMainWorld('electronAPI', electronAPI);
```

**为什么需要 Preload 脚本？**
1. **安全性**：防止渲染进程直接访问 Node.js API
2. **隔离**：主进程和渲染进程之间的安全通信
3. **类型安全**：提供强类型的 API 接口

### 3. 渲染进程（Vue 3 应用）

渲染进程运行 Vue 3 应用，通过 `window.electronAPI` 与主进程通信：

```vue
<!-- src/App.vue -->
<script setup lang="ts">
import { ref, onMounted } from 'vue';

const todos = ref([]);

// 通过 electronAPI 与主进程通信
onMounted(async () => {
  todos.value = await window.electronAPI.getTodos();
});

async function addTodo(text: string) {
  const newTodo = await window.electronAPI.addTodo(text);
  todos.value.push(newTodo);
}
</script>
```

### Vue 3 Composition API 优势

**1. 更好的代码组织**

```typescript
// 使用 Composition API
import { ref, computed, onMounted } from 'vue';

export default {
  setup() {
    // 逻辑分组更清晰
    const todos = ref([]);
    const filter = ref('all');

    const filteredTodos = computed(() => {
      // 计算逻辑
    });

    onMounted(() => {
      // 初始化逻辑
    });

    return { todos, filter, filteredTodos };
  }
}
```

**2. 逻辑复用**

```typescript
// 可复用的组合式函数
function useTodos() {
  const todos = ref([]);

  async function loadTodos() {
    todos.value = await window.electronAPI.getTodos();
  }

  async function addTodo(text: string) {
    const newTodo = await window.electronAPI.addTodo(text);
    todos.value.push(newTodo);
  }

  return { todos, loadTodos, addTodo };
}

// 在多个组件中使用
const { todos, loadTodos, addTodo } = useTodos();
```

**3. TypeScript 支持**

```typescript
// 完整的类型推导
interface Todo {
  id: number;
  text: string;
  completed: boolean;
}

const todos = ref<Todo[]>([]);  // 类型安全
const currentTodo = computed(() => todos.value[0]); // 自动推导为 Todo | undefined
```

### Vite 集成

Vite 为 Vue + Electron 开发提供了极速的开发体验：

```typescript
// vite.config.ts
import { defineConfig } from 'vite';
import vue from '@vitejs/plugin-vue';
import electron from 'vite-plugin-electron';

export default defineConfig({
  plugins: [
    vue(),
    electron([
      {
        entry: 'electron/main.ts',  // 主进程入口
        vite: {
          build: {
            outDir: 'dist-electron',
          },
        },
      },
      {
        entry: 'electron/preload.ts',  // Preload 入口
        vite: {
          build: {
            outDir: 'dist-electron',
          },
        },
      },
    ]),
  ],
});
```

**Vite 优势：**
- ⚡ 极速的 HMR（热模块替换）
- 📦 优化的生产构建
- 🔧 开箱即用的 TypeScript 支持
- 🎯 按需编译，启动速度快

## 与 Electron + React 的对比

### 详细对比表

| 特性 | Electron + Vue 3 | Electron + React | 说明 |
|------|-----------------|------------------|------|
| **学习曲线** | ⭐⭐⭐⭐⭐ 平缓 | ⭐⭐⭐ 中等 | Vue 更容易上手 |
| **模板语法** | 直观的模板语法 | JSX/TSX | Vue 模板更接近 HTML |
| **状态管理** | 响应式系统 + Pinia | useState/useContext/Redux | Vue 响应式更简单 |
| **双向绑定** | ✅ v-model | ❌ 需手动实现 | Vue 内置支持 |
| **包体积** | ~450KB (min+gzip) | ~550KB (min+gzip) | Vue 更轻量 |
| **性能** | ⭐⭐⭐⭐⭐ 优秀 | ⭐⭐⭐⭐ 良好 | 都很快，Vue 稍优 |
| **TypeScript** | ⭐⭐⭐⭐ 优秀 | ⭐⭐⭐⭐⭐ 卓越 | React 类型支持更成熟 |
| **生态系统** | ⭐⭐⭐⭐ 丰富 | ⭐⭐⭐⭐⭐ 最丰富 | React 生态更大 |
| **中文文档** | ⭐⭐⭐⭐⭐ 优秀 | ⭐⭐⭐⭐ 良好 | Vue 中文支持更好 |
| **开发体验** | ⭐⭐⭐⭐⭐ 出色 | ⭐⭐⭐⭐ 优秀 | Vue SFC 更直观 |

### 代码对比

#### 1. 组件定义

**Vue 3 (SFC - Single File Component)**

```vue
<template>
  <div class="todo-item">
    <input
      type="checkbox"
      v-model="todo.completed"
      @change="$emit('toggle', todo.id)"
    />
    <span :class="{ completed: todo.completed }">
      {{ todo.text }}
    </span>
    <button @click="$emit('delete', todo.id)">删除</button>
  </div>
</template>

<script setup lang="ts">
interface Todo {
  id: number;
  text: string;
  completed: boolean;
}

defineProps<{ todo: Todo }>();
defineEmits<{
  toggle: [id: number];
  delete: [id: number];
}>();
</script>

<style scoped>
.todo-item { padding: 1rem; }
.completed { text-decoration: line-through; }
</style>
```

**React (TSX)**

```tsx
interface TodoItemProps {
  todo: Todo;
  onToggle: (id: number) => void;
  onDelete: (id: number) => void;
}

function TodoItem({ todo, onToggle, onDelete }: TodoItemProps) {
  return (
    <div className="todo-item">
      <input
        type="checkbox"
        checked={todo.completed}
        onChange={() => onToggle(todo.id)}
      />
      <span className={todo.completed ? 'completed' : ''}>
        {todo.text}
      </span>
      <button onClick={() => onDelete(todo.id)}>删除</button>
    </div>
  );
}

// 需要单独的 CSS 文件
import './TodoItem.css';
```

#### 2. 状态管理

**Vue 3 - 响应式系统**

```typescript
import { ref, computed } from 'vue';

// 自动追踪依赖
const todos = ref<Todo[]>([]);
const filter = ref('all');

// 自动重新计算
const filteredTodos = computed(() => {
  if (filter.value === 'active') {
    return todos.value.filter(t => !t.completed);
  }
  return todos.value;
});

// 修改会自动触发更新
function addTodo(text: string) {
  todos.value.push({ id: Date.now(), text, completed: false });
}
```

**React - useState/useEffect**

```typescript
import { useState, useMemo } from 'react';

// 需要手动管理状态
const [todos, setTodos] = useState<Todo[]>([]);
const [filter, setFilter] = useState('all');

// 需要依赖数组
const filteredTodos = useMemo(() => {
  if (filter === 'active') {
    return todos.filter(t => !t.completed);
  }
  return todos;
}, [todos, filter]);

// 需要创建新数组
function addTodo(text: string) {
  setTodos([...todos, { id: Date.now(), text, completed: false }]);
}
```

#### 3. 条件渲染和列表渲染

**Vue 3**

```vue
<template>
  <!-- 条件渲染 -->
  <div v-if="todos.length > 0">
    有 {{ todos.length }} 个待办事项
  </div>
  <div v-else>
    没有待办事项
  </div>

  <!-- 列表渲染 -->
  <div v-for="todo in filteredTodos" :key="todo.id">
    <TodoItem :todo="todo" />
  </div>
</template>
```

**React**

```tsx
{/* 条件渲染 */}
{todos.length > 0 ? (
  <div>有 {todos.length} 个待办事项</div>
) : (
  <div>没有待办事项</div>
)}

{/* 列表渲染 */}
{filteredTodos.map(todo => (
  <TodoItem key={todo.id} todo={todo} />
))}
```

#### 4. 双向绑定

**Vue 3**

```vue
<template>
  <!-- 自动双向绑定 -->
  <input v-model="searchText" />
  <input v-model.number="count" />
  <input v-model.trim="username" />
</template>
```

**React**

```tsx
// 需要手动实现
<input
  value={searchText}
  onChange={(e) => setSearchText(e.target.value)}
/>
<input
  value={count}
  onChange={(e) => setCount(Number(e.target.value))}
/>
<input
  value={username}
  onChange={(e) => setUsername(e.target.value.trim())}
/>
```

### 选择建议

**选择 Vue 3 如果你：**
- 喜欢模板语法，想要更直观的开发体验
- 需要快速上手，学习曲线平缓
- 想要内置的双向绑定和指令系统
- 偏好单文件组件（SFC）的组织方式
- 需要优秀的中文文档和社区支持

**选择 React 如果你：**
- 偏好 JSX/TSX 的灵活性
- 已有 React 经验或团队使用 React
- 需要最大的生态系统和第三方库支持
- 更看重 TypeScript 类型推导
- 喜欢函数式编程风格

## 项目结构

```
electron-vue-todo/
├── electron/                    # Electron 主进程和 Preload
│   ├── main.ts                 # 主进程入口（窗口管理、IPC、菜单）
│   └── preload.ts              # Preload 脚本（contextBridge）
│
├── src/                        # Vue 3 渲染进程
│   ├── components/             # Vue 组件
│   │   ├── TodoInput.vue      # 输入组件
│   │   ├── TodoList.vue       # 列表组件
│   │   └── TodoItem.vue       # 单项组件
│   ├── types/                  # TypeScript 类型定义
│   │   └── index.ts           # 共享类型
│   ├── App.vue                # 根组件
│   ├── main.ts                # Vue 应用入口
│   └── style.css              # 全局样式
│
├── public/                     # 静态资源
│   └── icon.png               # 应用图标
│
├── build/                      # 构建资源（图标等）
│   ├── icon.icns              # macOS 图标
│   ├── icon.ico               # Windows 图标
│   └── icons/                 # Linux 图标
│
├── dist/                       # Vue 构建输出
├── dist-electron/              # Electron 构建输出
├── release/                    # 打包输出
│
├── index.html                  # HTML 模板
├── package.json                # 项目配置
├── vite.config.ts             # Vite 配置
├── electron-builder.json       # Electron Builder 配置
├── tsconfig.json              # TypeScript 配置（源代码）
├── tsconfig.node.json         # TypeScript 配置（Node 环境）
├── .gitignore                 # Git 忽略文件
└── README.md                  # 项目文档
```

### 文件说明

#### 核心文件

**electron/main.ts**
- 主进程入口
- 创建和管理 BrowserWindow
- 处理应用生命周期
- 定义 IPC 处理器
- 实现文件系统操作
- 创建原生菜单和托盘

**electron/preload.ts**
- 安全的 API 暴露
- contextBridge 实现
- IPC 通信封装
- 类型定义导出

**src/App.vue**
- Vue 应用根组件
- 全局状态管理
- IPC 通信调用
- 事件监听设置

**src/components/***
- TodoInput.vue：输入框组件，处理新待办添加
- TodoList.vue：列表容器组件，管理列表渲染
- TodoItem.vue：单个待办项组件，处理编辑和删除

**vite.config.ts**
- Vite 构建配置
- Electron 插件配置
- Vue 插件配置
- 路径别名设置

**electron-builder.json**
- 打包配置
- 平台特定设置
- 图标和资源配置
- 发布配置

## 快速开始

### 环境要求

- Node.js >= 18.0.0
- npm >= 9.0.0 或 pnpm >= 8.0.0
- Git

### 安装步骤

```bash
# 1. 克隆仓库
git clone https://github.com/yourusername/electron-vue-todo.git
cd electron-vue-todo

# 2. 安装依赖
npm install
# 或使用 pnpm
pnpm install

# 3. 启动开发服务器
npm run electron:dev

# 4. 构建生产版本
npm run build

# 5. 仅构建特定平台
npm run build:win    # Windows
npm run build:mac    # macOS
npm run build:linux  # Linux
```

### 开发模式

开发模式会同时启动 Vite 开发服务器和 Electron 应用：

```bash
npm run electron:dev
```

这会：
1. 启动 Vite 开发服务器（http://localhost:5173）
2. 启动 Electron 主进程
3. 打开开发者工具
4. 启用热模块替换（HMR）

### 生产构建

```bash
# 完整构建（当前平台）
npm run build

# Windows 平台
npm run build:win

# macOS 平台
npm run build:mac

# Linux 平台
npm run build:linux
```

构建输出位于 `release/` 目录。

## 开发指南

### 添加新功能

#### 1. 添加新的 IPC 通道

**步骤 1：在主进程定义处理器**

```typescript
// electron/main.ts
ipcMain.handle('custom-operation', async (_, arg1, arg2) => {
  // 处理逻辑
  return result;
});
```

**步骤 2：在 Preload 暴露 API**

```typescript
// electron/preload.ts
const electronAPI = {
  // ... 现有 API
  customOperation: (arg1: string, arg2: number) =>
    ipcRenderer.invoke('custom-operation', arg1, arg2),
};
```

**步骤 3：更新类型定义**

```typescript
// src/types/index.ts
export interface ElectronAPI {
  // ... 现有方法
  customOperation: (arg1: string, arg2: number) => Promise<Result>;
}
```

**步骤 4：在 Vue 组件中使用**

```vue
<script setup lang="ts">
async function handleCustom() {
  const result = await window.electronAPI.customOperation('test', 42);
  console.log(result);
}
</script>
```

#### 2. 添加新的 Vue 组件

```vue
<!-- src/components/NewComponent.vue -->
<template>
  <div class="new-component">
    <h2>{{ title }}</h2>
    <p>{{ description }}</p>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';

interface Props {
  title: string;
  description?: string;
}

const props = withDefaults(defineProps<Props>(), {
  description: '默认描述',
});

const emit = defineEmits<{
  action: [value: string];
}>();
</script>

<style scoped>
.new-component {
  padding: 1rem;
}
</style>
```

#### 3. 添加原生菜单项

```typescript
// electron/main.ts
function createMenu() {
  const template: Electron.MenuItemConstructorOptions[] = [
    {
      label: '新菜单',
      submenu: [
        {
          label: '新功能',
          accelerator: 'CmdOrCtrl+Shift+N',
          click: () => {
            // 执行操作或向渲染进程发送消息
            mainWindow?.webContents.send('trigger-new-feature');
          },
        },
      ],
    },
  ];

  const menu = Menu.buildFromTemplate(template);
  Menu.setApplicationMenu(menu);
}
```

### 调试技巧

#### 1. 调试主进程

在 VS Code 中添加调试配置：

```json
// .vscode/launch.json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Debug Main Process",
      "type": "node",
      "request": "launch",
      "cwd": "${workspaceFolder}",
      "runtimeExecutable": "${workspaceFolder}/node_modules/.bin/electron",
      "windows": {
        "runtimeExecutable": "${workspaceFolder}/node_modules/.bin/electron.cmd"
      },
      "args": ["."],
      "outputCapture": "std"
    }
  ]
}
```

#### 2. 调试渲染进程

在开发模式下，开发者工具会自动打开。你也可以：

```typescript
// 在主进程中手动打开
mainWindow.webContents.openDevTools();

// 在渲染进程中使用 Vue Devtools
// 安装 Vue Devtools 浏览器扩展
```

#### 3. 日志记录

```typescript
// 主进程
console.log('[Main]', 'message');

// 渲染进程
console.log('[Renderer]', 'message');

// 使用 electron-log 进行文件日志
import log from 'electron-log';
log.info('Application started');
```

## IPC 通信模式

### 1. 单向通信（Main → Renderer）

**使用场景**：主进程通知渲染进程

```typescript
// 主进程
mainWindow.webContents.send('notification', 'Hello from main');

// Preload
const electronAPI = {
  onNotification: (callback: (message: string) => void) => {
    ipcRenderer.on('notification', (_, message) => callback(message));
  },
};

// 渲染进程（Vue）
window.electronAPI.onNotification((message) => {
  console.log('Received:', message);
});
```

### 2. 请求-响应模式（Renderer → Main → Renderer）

**使用场景**：渲染进程请求数据

```typescript
// 主进程
ipcMain.handle('get-data', async (event, id) => {
  const data = await fetchDataFromDB(id);
  return data;
});

// Preload
const electronAPI = {
  getData: (id: number) => ipcRenderer.invoke('get-data', id),
};

// 渲染进程
const data = await window.electronAPI.getData(123);
```

### 3. 双向通信

**使用场景**：需要进度反馈的长时间操作

```typescript
// 主进程
ipcMain.handle('long-operation', async (event) => {
  for (let i = 0; i <= 100; i += 10) {
    event.sender.send('operation-progress', i);
    await delay(100);
  }
  return 'completed';
});

// Preload
const electronAPI = {
  startLongOperation: () => ipcRenderer.invoke('long-operation'),
  onProgress: (callback: (progress: number) => void) => {
    ipcRenderer.on('operation-progress', (_, progress) => callback(progress));
  },
};

// 渲染进程
window.electronAPI.onProgress((progress) => {
  console.log(`Progress: ${progress}%`);
});
await window.electronAPI.startLongOperation();
```

### 4. 最佳实践

#### ✅ 推荐

```typescript
// 使用 invoke/handle 进行异步通信
ipcMain.handle('async-operation', async () => {
  return await performAsyncTask();
});

// 使用类型安全的 API
interface ElectronAPI {
  getData: () => Promise<Data>;
}
```

#### ❌ 不推荐

```typescript
// 避免使用 send/on 进行请求-响应
// 这会导致回调地狱和难以追踪的错误

ipcRenderer.send('get-data-request');
ipcRenderer.on('get-data-response', (_, data) => {
  // 处理数据
});
```

## 安全最佳实践

### 1. Context Isolation（上下文隔离）

**必须启用**：防止渲染进程直接访问 Electron 内部和 Node.js API

```typescript
// electron/main.ts
webPreferences: {
  contextIsolation: true,  // ✅ 必须为 true
  nodeIntegration: false,   // ✅ 必须为 false
}
```

### 2. Node Integration（Node 集成）

**必须禁用**：防止恶意脚本执行 Node.js 代码

```typescript
webPreferences: {
  nodeIntegration: false,  // ✅ 禁用
}
```

### 3. Sandbox（沙箱）

**推荐启用**：提供额外的安全层

```typescript
webPreferences: {
  sandbox: true,  // ✅ 生产环境建议启用
}
```

### 4. Content Security Policy（CSP）

**必须配置**：防止 XSS 攻击

```html
<!-- index.html -->
<meta
  http-equiv="Content-Security-Policy"
  content="default-src 'self'; script-src 'self' 'unsafe-inline'; style-src 'self' 'unsafe-inline'; img-src 'self' data:;"
/>
```

### 5. 安全的 contextBridge 使用

```typescript
// ✅ 推荐：只暴露必要的 API
contextBridge.exposeInMainWorld('electronAPI', {
  getTodos: () => ipcRenderer.invoke('get-todos'),
  addTodo: (text: string) => ipcRenderer.invoke('add-todo', text),
});

// ❌ 危险：不要暴露整个 ipcRenderer
contextBridge.exposeInMainWorld('ipcRenderer', ipcRenderer);
```

### 6. 输入验证

```typescript
// 主进程：始终验证来自渲染进程的输入
ipcMain.handle('add-todo', async (_, text: unknown) => {
  if (typeof text !== 'string') {
    throw new Error('Invalid input: text must be a string');
  }

  if (text.length === 0 || text.length > 200) {
    throw new Error('Invalid input: text length must be 1-200');
  }

  // 处理有效输入
  return addTodoToDatabase(text);
});
```

### 7. 外部链接处理

```typescript
// 防止在应用内打开外部链接
mainWindow.webContents.setWindowOpenHandler(({ url }) => {
  shell.openExternal(url);  // 在默认浏览器中打开
  return { action: 'deny' }; // 阻止在应用内打开
});
```

### 8. 安全检查清单

- [ ] `contextIsolation: true`
- [ ] `nodeIntegration: false`
- [ ] `sandbox: true`（生产环境）
- [ ] 配置了 CSP
- [ ] 只通过 contextBridge 暴露必要的 API
- [ ] 验证所有来自渲染进程的输入
- [ ] 外部链接在浏览器中打开
- [ ] 不在渲染进程中执行任意代码
- [ ] 使用最新版本的 Electron
- [ ] 定期更新依赖包

## Vite + Electron 配置

### 配置解析

```typescript
// vite.config.ts
import { defineConfig } from 'vite';
import vue from '@vitejs/plugin-vue';
import electron from 'vite-plugin-electron';
import renderer from 'vite-plugin-electron-renderer';

export default defineConfig({
  plugins: [
    // Vue 3 支持
    vue(),

    // Electron 主进程和 Preload
    electron([
      {
        entry: 'electron/main.ts',
        onstart(options) {
          // 启动 Electron
          options.startup();
        },
        vite: {
          build: {
            outDir: 'dist-electron',
            rollupOptions: {
              external: ['electron'],  // 不打包 Electron
            },
          },
        },
      },
      {
        entry: 'electron/preload.ts',
        onstart(options) {
          // 重新加载 Preload
          options.reload();
        },
        vite: {
          build: {
            outDir: 'dist-electron',
          },
        },
      },
    ]),

    // Renderer 进程支持
    renderer(),
  ],

  // 路径别名
  resolve: {
    alias: {
      '@': path.resolve(__dirname, './src'),
    },
  },

  // 基础路径（生产环境使用相对路径）
  base: './',

  // 构建选项
  build: {
    outDir: 'dist',
    emptyOutDir: true,
    rollupOptions: {
      output: {
        manualChunks: {
          vue: ['vue'],  // 将 Vue 单独打包
        },
      },
    },
  },

  // 开发服务器配置
  server: {
    port: 5173,
    strictPort: true,  // 端口被占用时报错
  },
});
```

### 开发模式工作流程

```
1. 运行 npm run electron:dev
   ↓
2. Vite 启动开发服务器 (http://localhost:5173)
   ↓
3. vite-plugin-electron 编译 main.ts 和 preload.ts
   ↓
4. Electron 启动并加载 http://localhost:5173
   ↓
5. 文件修改时：
   - Vue 文件 → Vite HMR → 即时更新
   - main.ts → 重启 Electron
   - preload.ts → 重新加载页面
```

### 生产构建工作流程

```
1. 运行 npm run build
   ↓
2. vue-tsc 进行类型检查
   ↓
3. Vite 构建渲染进程 → dist/
   ↓
4. vite-plugin-electron 构建主进程 → dist-electron/
   ↓
5. electron-builder 打包应用 → release/
```

### 优化技巧

#### 1. 代码分割

```typescript
// vite.config.ts
build: {
  rollupOptions: {
    output: {
      manualChunks: {
        'vue': ['vue'],
        'vendor': ['other-large-dependency'],
      },
    },
  },
},
```

#### 2. 资源优化

```typescript
build: {
  assetsInlineLimit: 4096,  // 小于 4KB 的资源内联为 base64
  chunkSizeWarningLimit: 1000,  // chunk 大小警告阈值
},
```

#### 3. 预构建优化

```typescript
optimizeDeps: {
  include: ['vue', 'large-dependency'],
  exclude: ['electron'],
},
```

## 打包发布

### Electron Builder 配置详解

```json
{
  "appId": "com.electron.vue.todo",
  "productName": "Electron Vue Todo",
  "directories": {
    "output": "release/${version}"
  },
  "files": [
    "dist/**/*",
    "dist-electron/**/*"
  ],
  "mac": {
    "target": ["dmg", "zip"],
    "category": "public.app-category.productivity",
    "icon": "build/icon.icns",
    "hardenedRuntime": true,
    "gatekeeperAssess": false,
    "entitlements": "build/entitlements.mac.plist"
  },
  "win": {
    "target": ["nsis", "portable", "zip"],
    "icon": "build/icon.ico"
  },
  "linux": {
    "target": ["AppImage", "deb", "rpm"],
    "category": "Utility"
  }
}
```

### Windows 打包

```bash
# NSIS 安装程序 + 便携版 + ZIP
npm run build:win

# 输出文件：
# - Electron Vue Todo Setup 1.0.0.exe  (安装程序)
# - Electron Vue Todo 1.0.0.exe        (便携版)
# - Electron Vue Todo 1.0.0-win.zip    (ZIP 压缩包)
```

**NSIS 安装程序特性：**
- 用户可选择安装目录
- 创建桌面快捷方式
- 创建开始菜单快捷方式
- 支持卸载
- 可选择单用户或所有用户安装

### macOS 打包

```bash
# DMG 和 ZIP（支持 Intel 和 Apple Silicon）
npm run build:mac

# 输出文件：
# - Electron Vue Todo-1.0.0-arm64.dmg
# - Electron Vue Todo-1.0.0-x64.dmg
# - Electron Vue Todo-1.0.0-mac.zip
```

**代码签名（可选）：**

```bash
# 设置环境变量
export CSC_LINK=/path/to/certificate.p12
export CSC_KEY_PASSWORD=your-password
export APPLE_ID=your-apple-id@example.com
export APPLE_ID_PASSWORD=app-specific-password

# 构建并签名
npm run build:mac
```

### Linux 打包

```bash
# AppImage、DEB、RPM
npm run build:linux

# 输出文件：
# - Electron Vue Todo-1.0.0.AppImage
# - electron-vue-todo_1.0.0_amd64.deb
# - electron-vue-todo-1.0.0.x86_64.rpm
```

**包管理器安装：**

```bash
# Debian/Ubuntu
sudo dpkg -i electron-vue-todo_1.0.0_amd64.deb

# Red Hat/Fedora
sudo rpm -i electron-vue-todo-1.0.0.x86_64.rpm

# AppImage (直接运行)
chmod +x Electron\ Vue\ Todo-1.0.0.AppImage
./Electron\ Vue\ Todo-1.0.0.AppImage
```

### 图标准备

不同平台需要不同格式的图标：

```
build/
├── icon.icns          # macOS (至少 512x512)
├── icon.ico           # Windows (包含多个尺寸)
└── icons/             # Linux
    ├── 16x16.png
    ├── 32x32.png
    ├── 48x48.png
    ├── 64x64.png
    ├── 128x128.png
    ├── 256x256.png
    └── 512x512.png
```

**生成图标工具：**

```bash
# 使用 electron-icon-builder
npm install --save-dev electron-icon-builder

# package.json
{
  "scripts": {
    "generate-icons": "electron-icon-builder --input=./icon.png --output=./build"
  }
}
```

### 自动更新

```typescript
// electron/main.ts
import { autoUpdater } from 'electron-updater';

// 检查更新
autoUpdater.checkForUpdatesAndNotify();

// 监听更新事件
autoUpdater.on('update-available', () => {
  mainWindow?.webContents.send('update-available');
});

autoUpdater.on('update-downloaded', () => {
  mainWindow?.webContents.send('update-downloaded');
});

// IPC 处理器
ipcMain.handle('install-update', () => {
  autoUpdater.quitAndInstall();
});
```

**配置自动更新服务器：**

```json
// electron-builder.json
{
  "publish": [
    {
      "provider": "github",
      "owner": "your-username",
      "repo": "electron-vue-todo"
    }
  ]
}
```

### 发布到 GitHub Releases

```bash
# 1. 构建并发布
npm run build
GH_TOKEN=your-github-token npm run publish

# 2. 或使用 release-it
npm install --save-dev release-it
npm run release
```

## 性能优化

### 1. 启动性能

```typescript
// 延迟加载非关键模块
app.whenReady().then(() => {
  createWindow();

  // 延迟加载
  setTimeout(() => {
    initializeNonCriticalFeatures();
  }, 1000);
});
```

### 2. 渲染性能

```vue
<!-- 使用 v-show 代替 v-if 进行频繁切换 -->
<div v-show="isVisible">内容</div>

<!-- 使用 key 优化列表渲染 -->
<div v-for="todo in todos" :key="todo.id">
  {{ todo.text }}
</div>

<!-- 使用 v-once 渲染静态内容 -->
<div v-once>{{ staticContent }}</div>
```

### 3. 内存优化

```typescript
// 清理事件监听器
onUnmounted(() => {
  window.electronAPI.removeAllListeners();
});

// 限制列表大小
const MAX_TODOS = 1000;
if (todos.value.length > MAX_TODOS) {
  todos.value = todos.value.slice(0, MAX_TODOS);
}
```

### 4. 打包体积优化

```typescript
// vite.config.ts
build: {
  rollupOptions: {
    external: ['electron'],
    output: {
      manualChunks: {
        vue: ['vue'],
      },
    },
  },
  minify: 'terser',
  terserOptions: {
    compress: {
      drop_console: true,  // 移除 console
      drop_debugger: true, // 移除 debugger
    },
  },
},
```

## 故障排除

### 常见问题

#### 1. Electron 无法启动

**问题**：运行 `npm run electron:dev` 后没有窗口显示

**解决方案**：
```bash
# 检查端口是否被占用
lsof -i :5173

# 清除缓存
rm -rf node_modules dist dist-electron
npm install
```

#### 2. IPC 通信失败

**问题**：`window.electronAPI is undefined`

**解决方案**：
```typescript
// 确保 preload 脚本正确配置
webPreferences: {
  preload: path.join(__dirname, 'preload.js'),  // 注意是 .js 不是 .ts
}

// 检查构建输出
ls dist-electron/  # 应该包含 preload.js
```

#### 3. 热更新不工作

**问题**：修改代码后没有自动刷新

**解决方案**：
```bash
# 检查 Vite 配置
# 确保开发服务器正常运行
curl http://localhost:5173

# 重启开发服务器
npm run electron:dev
```

#### 4. 打包失败

**问题**：`electron-builder` 打包时报错

**解决方案**：
```bash
# 确保所有依赖已安装
npm install

# 清除缓存
npm run build -- --clean

# 检查 electron-builder.json 配置
```

#### 5. TypeScript 错误

**问题**：类型检查失败

**解决方案**：
```typescript
// 确保类型定义正确
// src/types/index.ts
declare global {
  interface Window {
    electronAPI: ElectronAPI;
  }
}

// 运行类型检查
npm run type-check
```

## 最佳实践

### 1. 项目组织

```
✅ 推荐
- 按功能模块组织组件
- 使用 Composition API
- 提取可复用逻辑到 composables
- 保持组件单一职责

❌ 避免
- 巨大的单体组件
- 全局状态滥用
- 过度嵌套的组件结构
```

### 2. 状态管理

```typescript
// ✅ 推荐：使用 Pinia（如果需要全局状态）
import { defineStore } from 'pinia';

export const useTodoStore = defineStore('todos', {
  state: () => ({
    todos: [] as Todo[],
  }),
  actions: {
    async loadTodos() {
      this.todos = await window.electronAPI.getTodos();
    },
  },
});

// ❌ 避免：过度使用全局状态
// 本地状态优先，只在必要时使用全局状态
```

### 3. 错误处理

```typescript
// ✅ 推荐：统一的错误处理
async function handleOperation() {
  try {
    const result = await window.electronAPI.someOperation();
    return result;
  } catch (error) {
    console.error('Operation failed:', error);
    showNotification('操作失败，请重试');
    throw error;  // 继续抛出以便上层处理
  }
}

// ❌ 避免：忽略错误
async function badOperation() {
  const result = await window.electronAPI.someOperation();
  // 没有错误处理！
}
```

### 4. 性能考虑

```vue
<!-- ✅ 推荐：计算属性缓存 -->
<script setup>
const filteredTodos = computed(() => {
  return todos.value.filter(/* ... */);
});
</script>

<!-- ❌ 避免：在模板中进行复杂计算 -->
<template>
  <div v-for="todo in todos.filter(/* ... */)" :key="todo.id">
    <!-- 每次渲染都会重新过滤 -->
  </div>
</template>
```

## 进阶主题

### 1. 自定义协议

```typescript
// 注册自定义协议
app.setAsDefaultProtocolClient('electron-vue-todo');

// 处理协议 URL
app.on('open-url', (event, url) => {
  event.preventDefault();
  // 解析 URL 并执行相应操作
  const params = new URL(url).searchParams;
  mainWindow?.webContents.send('handle-protocol', params);
});
```

### 2. 原生模块集成

```typescript
// 使用原生 Node.js 模块
import { readFileSync } from 'fs';
import { join } from 'path';

// 注意：只能在主进程或 Preload 中使用
const data = readFileSync(join(__dirname, 'data.json'), 'utf-8');
```

### 3. 多窗口管理

```typescript
let secondWindow: BrowserWindow | null = null;

function createSecondWindow() {
  secondWindow = new BrowserWindow({
    width: 600,
    height: 400,
    parent: mainWindow!,  // 设置父窗口
    modal: true,          // 模态窗口
  });

  secondWindow.loadFile('second.html');
}

// IPC 通信
ipcMain.handle('open-second-window', () => {
  createSecondWindow();
});
```

### 4. 系统集成

```typescript
// macOS Touch Bar
import { TouchBar } from 'electron';

const touchBar = new TouchBar({
  items: [
    new TouchBar.TouchBarButton({
      label: '新建待办',
      click: () => {
        mainWindow?.webContents.send('focus-input');
      },
    }),
  ],
});

mainWindow.setTouchBar(touchBar);

// Windows Taskbar Progress
mainWindow.setProgressBar(0.5);  // 50%
mainWindow.setProgressBar(-1);   // 移除进度条
```

## 常见问题

### Q1: 如何选择 Vue 还是 React？

A: 参考"与 Electron + React 的对比"章节。简而言之：
- Vue：更简单、更直观、学习曲线平缓
- React：生态更大、TypeScript 支持更好、社区更活跃

### Q2: 为什么要使用 contextBridge？

A: 安全性。contextBridge 提供了主进程和渲染进程之间的安全通信机制，防止恶意代码访问 Electron 内部 API 或 Node.js 功能。

### Q3: 如何减小打包体积？

A:
1. 使用代码分割
2. 移除未使用的依赖
3. 启用压缩和混淆
4. 使用 `asar: true`
5. 排除不必要的文件

### Q4: 如何实现自动更新？

A: 使用 `electron-updater`，参考"自动更新"章节。

### Q5: 开发模式下如何调试？

A:
- 渲染进程：使用开发者工具（自动打开）
- 主进程：使用 VS Code 调试器（参考"调试技巧"）

### Q6: 如何处理不同平台的差异？

A:
```typescript
import { platform } from 'os';

if (platform() === 'darwin') {
  // macOS 特定代码
} else if (platform() === 'win32') {
  // Windows 特定代码
} else {
  // Linux 特定代码
}
```

### Q7: 如何优化启动速度？

A:
1. 延迟加载非关键模块
2. 减少依赖数量
3. 使用 V8 快照
4. 优化资源加载

### Q8: Vue 3 Composition API vs Options API？

A: 本项目使用 Composition API，因为：
- 更好的 TypeScript 支持
- 更灵活的代码组织
- 更容易复用逻辑
- 更好的性能

但如果你更熟悉 Options API，也可以使用。

## 贡献指南

欢迎贡献！请遵循以下步骤：

1. Fork 本仓库
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启 Pull Request

### 代码规范

- 使用 TypeScript
- 遵循 ESLint 规则
- 编写清晰的注释
- 添加必要的类型定义
- 确保所有测试通过

### 提交信息规范

```
feat: 添加新功能
fix: 修复 bug
docs: 文档更新
style: 代码格式调整
refactor: 代码重构
test: 测试相关
chore: 构建或辅助工具变动
```

## 许可证

MIT License - 詳見 [LICENSE](../../LICENSE) 文件

## 相关资源

### 官方文档

- [Electron 文档](https://www.electronjs.org/docs)
- [Vue 3 文档](https://cn.vuejs.org/)
- [Vite 文档](https://cn.vitejs.dev/)
- [TypeScript 文档](https://www.typescriptlang.org/docs/)
- [Electron Builder 文档](https://www.electron.build/)

### 推荐阅读

- [Electron 安全指南](https://www.electronjs.org/docs/latest/tutorial/security)
- [Vue 3 迁移指南](https://v3-migration.vuejs.org/)
- [Composition API 指南](https://cn.vuejs.org/guide/extras/composition-api-faq.html)

### 社区

- [Electron 中文社区](https://github.com/electron/electron/tree/main/docs-translations/zh-CN)
- [Vue.js 中文社区](https://github.com/vuejs/vue)
- [Stack Overflow - Electron](https://stackoverflow.com/questions/tagged/electron)
- [Stack Overflow - Vue.js](https://stackoverflow.com/questions/tagged/vue.js)

## 致谢

感谢所有开源贡献者，特别是：

- Electron 团队
- Vue.js 团队
- Vite 团队
- 所有依赖包的维护者

---

**Happy Coding! 🚀**

如果这个项目对你有帮助，请给个 ⭐ Star！

有问题？[提交 Issue](https://github.com/yourusername/electron-vue-todo/issues)
