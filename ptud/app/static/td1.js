document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('add-task-form');
    const input = document.getElementById('task-input');
    const toDoList = document.querySelector('.to-do-list');

    function loadTasks() {
        const tasks = JSON.parse(localStorage.getItem('tasks')) || [];
        tasks.forEach(task => {
            const newItem = createNewItem(task.task, task.completed); // Truyền vào cả nội dung và trạng thái hoàn thành của công việc
            toDoList.appendChild(newItem);
        });
    }

    function createNewItem(task, completed) {
        const newItem = document.createElement('li');
        newItem.classList.add('item');
        if (completed) {
            newItem.classList.add('completed'); // Thêm class 'completed' nếu công việc đã hoàn thành
        }
        newItem.innerHTML = `
            <input type="checkbox" ${completed ? 'checked' : ''}> <!-- Đánh dấu checkbox là đã được tích nếu công việc đã hoàn thành -->
            <label>${task}</label>
            <button class="delete">Xóa</button>
        `;
        return newItem;
    }

    loadTasks();

    form.addEventListener('submit', function(event) {
        event.preventDefault();

        const inputValue = input.value.trim();
        if (inputValue !== '') {
            const newItem = createNewItem(inputValue, false); // Mặc định công việc chưa hoàn thành khi thêm mới
            toDoList.appendChild(newItem);
            saveTask(inputValue, false); // Lưu trạng thái hoàn thành là false khi thêm mới công việc
            input.value = '';
        }
    });

    toDoList.addEventListener('click', function(event) {
        if (event.target.tagName === 'INPUT' && event.target.type === 'checkbox') {
            const listItem = event.target.closest('.item');
            listItem.classList.toggle('completed');
            updateLocalStorage();
        } else if (event.target.classList.contains('delete')) {
            const listItem = event.target.closest('.item');
            listItem.remove();
            updateLocalStorage();
        }
    });

    function saveTask(task, completed) {
        const tasks = JSON.parse(localStorage.getItem('tasks')) || [];
        tasks.push({ task: task, completed: completed });
        localStorage.setItem('tasks', JSON.stringify(tasks));
    }

    function updateLocalStorage() {
        const tasks = [];
        document.querySelectorAll('.item').forEach(item => {
            const taskText = item.querySelector('label').textContent;
            const completed = item.classList.contains('completed');
            tasks.push({ task: taskText, completed: completed });
        });
        localStorage.setItem('tasks', JSON.stringify(tasks));
    }
});
