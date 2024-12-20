import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
import java.util.*;

class Student {
    private int id;
    private String name;
    private double cgpa;

    public Student(int id, String name, double cgpa) {
        this.id = id;
        this.name = name;
        this.cgpa = cgpa;
    }

    public int getID() {
        return id;
    }

    public String getName() {
        return name;
    }

    public double getCGPA() {
        return cgpa;
    }
}

class Priorities {
    public List<Student> getStudents(List<String> events) {
        Comparator<Student> comparator = new Comparator<Student>() {
            @Override
            public int compare(Student s1, Student s2) {
                if (s1.getCGPA() != s2.getCGPA()) {
                    return Double.compare(s2.getCGPA(), s1.getCGPA());
                } else if (!s1.getName().equals(s2.getName())) {
                    return s1.getName().compareTo(s2.getName());
                } else {
                    return Integer.compare(s1.getID(), s2.getID());
                }
            }
        };

        PriorityQueue<Student> queue = new PriorityQueue<Student>(11, comparator);

        for (String event : events) {
            String[] eventDetails = event.split(" ");
            if (eventDetails[0].equals("ENTER")) {
                String name = eventDetails[1];
                double cgpa = Double.parseDouble(eventDetails[2]);
                int id = Integer.parseInt(eventDetails[3]);
                queue.add(new Student(id, name, cgpa));
            } else if (eventDetails[0].equals("SERVED")) {
                queue.poll();
            }
        }

        List<Student> students = new ArrayList<Student>();
        while (!queue.isEmpty()) {
            students.add(queue.poll());
        }
        return students;
    }
}

public class Solution {
    private final static Scanner scan = new Scanner(System.in);
    private final static Priorities priorities = new Priorities();
    
    public static void main(String[] args) {
        int totalEvents = Integer.parseInt(scan.nextLine());    
        List<String> events = new ArrayList<>();
        
        while (totalEvents-- != 0) {
            String event = scan.nextLine();
            events.add(event);
        }
        
        List<Student> students = priorities.getStudents(events);
        
        if (students.isEmpty()) {
            System.out.println("EMPTY");
        } else {
            for (Student st: students) {
                System.out.println(st.getName());
            }
        }
    }
}