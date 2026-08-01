import Alpine from 'alpinejs';
import './style.css';

// Storage key constant matching PROJECT.md interface contract
const STORAGE_KEY = 'todolistdemo_alpine_todos';

window.Alpine = Alpine;

Alpine.data('todoApp', () => ({
  // State
  todos: [],
  newTodo: '',
  filter: 'all', // 'all' | 'active' | 'completed'
  editingId: null,
  editText: '',

  // Lifecycle initialization
  init() {
    this.load();
  },

  // Load from LocalStorage
  load() {
    const saved = localStorage.getItem(STORAGE_KEY);
    if (saved) {
      try {
        this.todos = JSON.parse(saved);
      } catch (e) {
        console.error('Failed to parse saved todos from LocalStorage:', e);
        this.todos = [];
      }
    } else {
      // Default initial sample todos
      this.todos = [
        {
          id: '1',
          text: '學習 Alpine.js 3 核心響應式指令 (x-data, x-for, x-model)',
          completed: true,
          createdAt: Date.now() - 3600000
        },
        {
          id: '2',
          text: '實作 LocalStorage 資料持久化保存 (todolistdemo_alpine_todos)',
          completed: false,
          createdAt: Date.now() - 1800000
        },
        {
          id: '3',
          text: '體驗輕量級 DOM 宣告式驅動框架的極致靈活性',
          completed: false,
          createdAt: Date.now()
        }
      ];
      this.save();
    }
  },

  // Save to LocalStorage
  save() {
    try {
      localStorage.setItem(STORAGE_KEY, JSON.stringify(this.todos));
    } catch (e) {
      console.error('Failed to save todos to LocalStorage:', e);
    }
  },

  // Actions
  addTodo() {
    const text = this.newTodo.trim();
    if (!text) return;

    this.todos.push({
      id: Date.now().toString(),
      text: text,
      completed: false,
      createdAt: Date.now()
    });

    this.newTodo = '';
    this.save();
  },

  removeTodo(id) {
    this.todos = this.todos.filter((todo) => todo.id !== id);
    if (this.editingId === id) {
      this.cancelEdit();
    }
    this.save();
  },

  toggleTodo(id) {
    const todo = this.todos.find((t) => t.id === id);
    if (todo) {
      todo.completed = !todo.completed;
      this.save();
    }
  },

  toggleAll() {
    const targetState = !this.allCompleted;
    this.todos.forEach((todo) => {
      todo.completed = targetState;
    });
    this.save();
  },

  clearCompleted() {
    this.todos = this.todos.filter((todo) => !todo.completed);
    this.save();
  },

  startEdit(todo) {
    this.editingId = todo.id;
    this.editText = todo.text;
  },

  cancelEdit() {
    this.editingId = null;
    this.editText = '';
  },

  saveEdit(todo) {
    if (this.editingId !== todo.id) return;
    const text = this.editText.trim();
    if (!text) {
      this.removeTodo(todo.id);
    } else {
      todo.text = text;
      this.editingId = null;
      this.editText = '';
      this.save();
    }
  },

  // Computed Properties (Getters)
  get filteredTodos() {
    if (this.filter === 'active') {
      return this.todos.filter((todo) => !todo.completed);
    }
    if (this.filter === 'completed') {
      return this.todos.filter((todo) => todo.completed);
    }
    return this.todos;
  },

  get remainingCount() {
    return this.todos.filter((todo) => !todo.completed).length;
  },

  get hasCompleted() {
    return this.todos.some((todo) => todo.completed);
  },

  get allCompleted() {
    return this.todos.length > 0 && this.todos.every((todo) => todo.completed);
  }
}));

Alpine.start();
