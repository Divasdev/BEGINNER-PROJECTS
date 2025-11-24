const addBtn=document.getElementById("add-btn");
const taskInput=document.getElementById("task-input");
window.addEventListener("DOMContentLoaded", loadTasksFromStorage);

let taskList = JSON.parse(localStorage.getItem("tasks")) || [];
function addTask(){
     task=taskInput.value;
     if (task.trim() === "") {
         alert("Please add a task.");
         return;
     }

     

    const div = document.createElement("div");
    div.classList.add("task-container");
    div.innerHTML = `
        <p class="task-item">
            <input type="checkbox" class="checkbox-task">
            <span>${task}</span>
            <button class="delete-btn">DELETE</button>
        </p>
    `;

     taskList.push(task)
     localStorage.setItem("tasks", JSON.stringify(taskList));

     console.log(taskList);
     const taskListContainer = document.getElementById("task-list");
     taskListContainer.appendChild(div);
    



     const checkbox = div.querySelector(".checkbox-task");
     const textSpan = div.querySelector("span");
     const deleteBtn = div.querySelector(".delete-btn");

     checkbox.addEventListener("change", () => {
         if (checkbox.checked) {
             textSpan.style.textDecoration = "line-through";
             textSpan.style.opacity = "0.6";
         } else {
             textSpan.style.textDecoration = "none";
             textSpan.style.opacity = "1";
         }
     });

     deleteBtn.addEventListener("click", () => {
         taskList = taskList.filter(t => t !== task);
         localStorage.setItem("tasks", JSON.stringify(taskList));
         div.remove();
     });

     taskInput.value = "";

}
function loadTasksFromStorage() {
    const taskListContainer = document.getElementById("task-list");

    taskList.forEach((task) => {
        const div = document.createElement("div");
        div.classList.add("task-container");
        div.innerHTML = `
            <p class="task-item">
                <input type="checkbox" class="checkbox-task">
                <span>${task}</span>
                <button class="delete-btn">DELETE</button>
            </p>
        `;

        taskListContainer.appendChild(div);

        const checkbox = div.querySelector(".checkbox-task");
        const textSpan = div.querySelector("span");
        const deleteBtn = div.querySelector(".delete-btn");

        checkbox.addEventListener("change", () => {
            if (checkbox.checked) {
                textSpan.style.textDecoration = "line-through";
                textSpan.style.opacity = "0.6";
            } else {
                textSpan.style.textDecoration = "none";
                textSpan.style.opacity = "1";
            }
        });

        deleteBtn.addEventListener("click", () => {
            div.remove();
            taskList = taskList.filter(t => t !== task);
            localStorage.setItem("tasks", JSON.stringify(taskList));
        });
    });
}
