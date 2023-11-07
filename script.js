document.addEventListener("DOMContentLoaded", function () {
    // Event listener for when HTML content is loaded, gets references for HTML elements
    const taskInput = document.getElementById("ToDoInput");
    const addTaskButton = document.getElementById("addBtn");
    const taskList = document.getElementById("ToDoList");
    const deleteCompletedButton = document.getElementById("deleteBtn");

    // Event listener to add a task to To-Do List when button is clicked
    addTaskButton.addEventListener("click", function () {
        const taskText = taskInput.value.trim();
        if (taskText === "") return;

        // Creates checkbox style list items
        const li = document.createElement("li");
        const checkbox = document.createElement("input");
        checkbox.type = "checkbox";
        const taskLabel = document.createElement("label");
        taskLabel.textContent = taskText;
        // Appends list items to HTML document
        li.appendChild(checkbox);
        li.appendChild(taskLabel);
        taskList.appendChild(li);
        // Clears the input field once a task is added
        taskInput.value = "";
    });
    // Event listener to clear the input field when Delete button is clicked
    deleteCompletedButton.addEventListener("click", function () {
        const completedTasks = document.querySelectorAll('input[type="checkbox"]:checked');
        completedTasks.forEach((task) => {
            task.parentNode.remove();
        });
    });
});
