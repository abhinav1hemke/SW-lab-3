/**
 * Manually written Student class with only the behavior used in this example.
 */
public class Student {
    private final int id;
    private final String name;
    private final String course;

    public Student(int id, String name, String course) {
        this.id = id;
        this.name = name;
        this.course = course;
    }

    public void displayStudent() {
        System.out.println("Student ID: " + id);
        System.out.println("Name: " + name);
        System.out.println("Course: " + course);
    }

    public static void main(String[] args) {
        Student student = new Student(1, "Asha", "Computer Science");
        student.displayStudent();
    }
}
