/**
 * Example Student class showing common AI-generated Java boilerplate.
 */
public class Student {
    private int id;
    private String name;
    private String course;

    public Student() {
        this(1, "Asha", "Computer Science");
    }

    public Student(int id, String name, String course) {
        this.id = id;
        this.name = name;
        this.course = course;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getCourse() {
        return course;
    }

    public void setCourse(String course) {
        this.course = course;
    }

    public void displayStudent() {
        System.out.println("Student ID: " + id);
        System.out.println("Name: " + name);
        System.out.println("Course: " + course);
    }

    public static void main(String[] args) {
        Student student = new Student();
        student.displayStudent();
    }
}
