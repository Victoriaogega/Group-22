//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
fun main() {

    val taskSchedule=hashMapOf("Cleaning the house" to 1400,"Cook Breakfast" to 1000, "Washing my clothes" to 1900, "Do Python assignment" to 2200 )
    val sortedDeadlines=taskSchedule.entries.sortedBy { it.value }
    println(" John, your tasks for today are: $sortedDeadlines")
}