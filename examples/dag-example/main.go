package main

import (
	"fmt"
	"log"
	"time"

	"github.com/otiai10/task"
)

// Task represents a single task in the DAG.
type Task struct {
	Name      string
	DependsOn []string
	Func      func() error
}

// Run executes the DAG.
func Run(tasks []Task) error {
	t := task.New()
	for _, task := range tasks {
		t.Add(task.Name, task.Func, task.DependsOn...)
	}

	err := t.Run()
	if err != nil {
		return err
	}

	return nil
}

// ExampleTask1 demonstrates a simple task.
func ExampleTask1() error {
	fmt.Println("Executing ExampleTask1")
	return nil
}

// ExampleTask2 depends on ExampleTask1.
func ExampleTask2() error {
	fmt.Println("Executing ExampleTask2")
	return nil
}

// ExampleTask3 depends on ExampleTask2.
func ExampleTask3() error {
	fmt.Println("Executing ExampleTask3")
	return nil
}

func main() {
	tasks := []Task{
		{Name: "ExampleTask1", Func: ExampleTask1},
		{Name: "ExampleTask2", DependsOn: []string{"ExampleTask1"}, Func: ExampleTask2},
		{Name: "ExampleTask3", DependsOn: []string{"ExampleTask2"}, Func: ExampleTask3},
	}

	if err := Run(tasks); err != nil {
		log.Fatalf("Failed to run DAG: %v", err)
	}
}