// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract StudentData {

    // Structure to store student details
    struct Student {
        uint rollNo;
        string name;
        uint marks;
    }

    // Dynamic array of Students
    Student[] public students;

    // Add a student to array
    function addStudent(uint _rollNo, string memory _name, uint _marks) public {
        students.push(Student(_rollNo, _name, _marks));
    }

    // Get student by index
    function getStudent(uint index) public view returns(uint, string memory, uint) {
        require(index < students.length, "Invalid index");
        Student memory s = students[index];
        return (s.rollNo, s.name, s.marks);
    }

    // Get total students
    function totalStudents() public view returns(uint) {
        return students.length;
    }

    // Fallback Function to catch Ether or undefined function calls
    fallback() external payable {
        // you can keep empty or log event
    }

    // Receive Ether (optional)
    receive() external payable {}
}
