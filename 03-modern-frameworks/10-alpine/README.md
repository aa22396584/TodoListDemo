# Alpine.js Todo List — 輕量級 HTML 優先響應式框架

本模組為 **TodoListDemo** 專案中 **03-modern-frameworks** 分類下的 **Alpine.js 3** 待辦事項應用實現。展示 Alpine.js 宣告式 DOM 指令、零 Bundle 負擔與無 Virtual DOM 的極輕量響應式架構。

---

## 📚 目錄

- [技術棧與特性](#技術棧與特性)
- [Alpine.js 核心架構解析](#alpinejs-核心架構解析)
- [核心指令使用說明](#核心指令使用說明)
- [LocalStorage 資料持久化](#localstorage-資料持久化)
- [專案目錄結構](#專案目錄結構)
- [快速開始與構建命令](#快速開始與構建命令)
- [Alpine.js 與現代前端框架對比](#alpinejs-與現代前端框架對比)
- [學習重點與心得](#學習重點與心得)

---

## 🚀 技術棧與特性

- **Alpine.js 3.13+** — 極輕量（~4KB gzipped）HTML 優先 JavaScript 響應式框架
- **Vite 5.1+** — 現代化前端開發與打包構建工具
- **CSS3 Design Tokens** — 原生 CSS 變數、漸變視覺樣式與響應式佈局
- **LocalStorage API** — 瀏覽器端狀態持久化保存

---

## 💡 Alpine.js 核心架構解析

Alpine.js 經常被譽為「現代前端開發的 Tailwind CSS for JavaScript」。它不需要繁重的單文件組件 (SFC) 編譯過程，也不依賴 Virtual DOM 重繪，而是直接在 HTML 標籤上聲明響應式行為。

### 1. 基於 Vue 響應式引擎
Alpine.js 3 底層採用了 Vue 3 的 `@vue/reactivity` 模組，透過 JavaScript `Proxy` 實現細粒度狀態追蹤。當 `x-data` 狀態屬性發生變更時，Alpine.js 能精確更新對應的 DOM 節點。

### 2. HTML 優先 (HTML-First) 宣告式語法
不同於 React/SolidJS 的 JSX 或 Svelte 的獨立組件文件，Alpine.js 將狀態與邏輯直接與 HTML 結構緊密結合：

```html
<div x-data="{ count: 0 }">
  <button @click="count++">Increment</button>
  <span x-text="count"></span>
</div>
```

---

## 🛠️ 核心指令使用說明

本模組完整實現了 Alpine.js 核心響應式指令與 event listeners：

| 指令 | 說明 | 本模組範例應用 |
|---|---|---|
| `x-data` | 定義組件狀態與邏輯作用域 | `x-data="todoApp()"` 綁定 Alpine.data 組件 |
| `x-for` | 列表渲染迭代器 (需搭配 `<template>`) | `<template x-for="todo in filteredTodos" :key="todo.id">` |
| `x-model` | 雙向資料綁定 | `x-model="newTodo"` 與 `x-model="editText"` |
| `@click` | 點擊事件監聽 (v-on 簡寫) | `@click="addTodo()"`, `@click="clearCompleted()"` |
| `@keyup.enter` | 按鍵 Enter 監聽事件 | `@keyup.enter="addTodo()"`, `@keyup.enter="saveEdit(todo)"` |
| `x-show` | 條件顯示/隱藏 (CSS `display: none`) | `x-show="todos.length > 0"`, `x-show="hasCompleted"` |
| `:class` / `x-bind:class` | 動態類別樣式綁定 | `:class="{ completed: todo.completed, editing: editingId === todo.id }"` |
| `x-text` | 動態更新文字內容 | `<strong x-text="remainingCount"></strong>` |

---

## 💾 LocalStorage 資料持久化

本模組貫徹 **TodoListDemo** 通用 Key 命名規範：

- **Storage Key**: `todolistdemo_alpine_todos`
- **資料結構**:
  ```json
  [
    {
      "id": "1722518400000",
      "text": "學習 Alpine.js 3 核心響應式指令",
      "completed": false,
      "createdAt": 1722518400000
    }
  ]
  ```
- **自動載入與儲存**:
  在 `todoApp()` 初始化方法 `init()` 中自動從 `localStorage` 讀取資料；每當執行新增 (`addTodo`)、刪除 (`removeTodo`)、切換狀態 (`toggleTodo` / `toggleAll`)、清除完成 (`clearCompleted`) 或編輯 (`saveEdit`) 時，均會調用 `save()` 將當前狀態序列化存回 `localStorage`。

---

## 📁 專案目錄結構

```
03-modern-frameworks/10-alpine/
├── index.html        # Alpine.js DOM 標籤與 HTML-First 介面模板
├── package.json      # Vite 構建配置與 alpinejs 依賴定義
├── README.md         # 模組架構說明文件（本文件）
└── src/
    ├── app.js        # Alpine.data('todoApp', ...) 組件邏輯與狀態定義
    └── style.css     # 響應式現代化 UI 樣式表
```

---

## ⚡ 快速開始與構建命令

### 1. 安裝專案依賴

```bash
npm install
```

### 2. 啟動開發伺服器

```bash
npm run dev
```
開啟瀏覽器訪問控制台輸出的開發網址（例如 `http://localhost:5173`）。

### 3. 構建生產環境產物

```bash
npm run build
```
構建產物將輸出至 `dist/` 目錄。

### 4. 預覽生產構建產物

```bash
npm run preview
```

---

## 📊 Alpine.js 與現代前端框架對比

| 比較維度 | Alpine.js 3 | Svelte 4 | SolidJS | React 18 | Vue 3 |
|---|---|---|---|---|---|
| **Bundle 大小** | **~4 KB** (超輕量) | ~2 KB (編譯產物) | ~7 KB | ~42 KB | ~33 KB |
| **Virtual DOM** | ❌ **無** | ❌ **無** | ❌ **無** | ✅ 有 | ✅ 有 |
| **編譯步驟** | ⚡ **可選** (CDN即用) | ⚠️ **必須** | ⚠️ **必須** | ⚠️ **必須** | ⚠️ 可選 |
| **語法風格** | HTML 宣告式指令 | .svelte 組件 | JSX (Signals) | JSX (Hooks) | Vue SFC |
| **適用場景** | 漸進式增強、Server-rendered HTML (MPA)、微前端 | 小型至大型 SPA | 極致性能 SPA | 大型複雜企業應用 | 通用 SPA / SSR |

---

## 🎯 學習重點與心得

1. **極簡漸進式增強**: Alpine.js 能以極低成本侵入現有 HTML/服务端渲染（如 Django, Laravel, Rails）網頁，無需建置複雜的前端工具鏈即可賦予網頁強大的響應式互動能力。
2. **直覺的狀態管理**: 透過 `Alpine.data` 配合 getter 計算屬性 (`filteredTodos`, `remainingCount`)，能以高可讀性維護代碼狀態。
3. **無縫整合 Vite**: 在開發階段使用 Vite 進行 HMR 快速熱更新，在生產構建階段進行 Tree-shaking 打包，同時保留 Alpine.js 原生 HTML 標籤寫法的靈活性。

---

> 🏠 返回專案首頁：[TodoListDemo](../../README.md)

