package com.example.tomcattest;

public class Student{
private Integer id;
private String name;

        public Integer getId() {
                return id;
        }

        public String getName() {
                return name;
        }

        public Integer getAge() {
                return age;
        }

        public String getPhone() {
                return phone;
        }

        private Integer age;
private String phone;

public Student(Integer id, String name, Integer age, String phone){
        this.id = id;
        this.name = name;
        this.age = age;
        this.phone = phone;
        }
}