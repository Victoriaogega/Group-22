        class TaskSchedule{
    constructor(){
        this.tasks = new Map();
    }

    addTask(taskName, priority, deadline){
        this.tasks.set(taskName,{ priority,deadline});
        this.sortTasks();
    }
    getAllTasks(){
        return Array.from(this.tasks, ([name, details])=>({name, ...details}));
      

    }
    sortTasks(){
        this.tasks = new Map([...this.tasks.entries()].sort(this.compareTasks));

    }
    compareTasks(a,b){
        const[, taskA] = a;
        const[, taskB] = b;

        if (taskA.priority !== taskB.priority) {
            return taskA.priority - taskB.priority;
        }
        return taskA.deadline - taskB.deadline;
    }
}

const schedule = new TaskSchedule();

schedule.addTask("Task 1", 2, ("2025-05-21"));   
schedule.addTask("Task 2", 1, ("2025-05-22"));  
schedule.addTask("Task 3", 3, ("2025-05-22"));          
schedule.addTask("Task 4", 1, ("2025-05-22"));  

console.log("All tasks:",schedule.getAllTasks());