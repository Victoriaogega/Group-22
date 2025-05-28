fun main() {

    val taskSchedule=hashMapOf("Cleaning the house" to 1400,"Cook Breakfast" to 1000, "Washing my clothes" to 1900, "Do Python assignment" to 2200, "Clean the house." to 2400 )
    val sortedDeadlines=taskSchedule.entries.sortedBy { it.value }
    println(" John, your tasks for today are: $sortedDeadlines")

}