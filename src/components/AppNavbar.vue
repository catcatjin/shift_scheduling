<template>
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
      <div class="container">
        <a class="navbar-brand" href="#">護士排班系統</a>
        <button
          class="navbar-toggler"
          type="button"
          data-toggle="collapse"
          data-target="#navbarNav"
          aria-controls="navbarNav"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
          <ul class="navbar-nav">
            <li class="nav-item">
              <a class="nav-link" href="#">排班表</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="#">人員管理</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="#">設置</a>
            </li>
          </ul>
        </div>
      </div>
    </nav>
  </template>
  
  <script>
  export default {
    // Vue.js 組件選項，如 data、methods 等
    name: 'AppNavbar',
  };
  </script>
  
  <style scoped>
    /* 自定義 Navbar 組件的 CSS 樣式 */
  </style>