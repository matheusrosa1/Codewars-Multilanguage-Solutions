<?php

$method = $_SERVER["REQUEST_METHOD"];
$uri = $_SERVER["REQUEST_URI"];

$controller = new TaskController();

if ($uri == '/tasks' && $method == 'GET') {
  $controller-> getTasks();
} else if ($uri == 'tasks' && $method == 'POST') {
  $controller-> createTask();
}


class TaskModel
{
  private $tasks;

  public function __construct()
  {
    $this->tasks = [
      ['id' => 1, 'title' => 'Estudar php', 'description' => 'Treinar API']
    ];
  }

  public function getAll()
  {
    return $this->tasks;
  }

  public function add($title, $descrition)
  {
    $this->tasks[] = [
      "id" => count($this->tasks) + 1,
      "title" => $title,
      "description" => $descrition
    ];
  }
}

class TaskController
{
  private $model;

  public function __construct()
  {
    $this->model = new TaskModel();
  }

  public function getTasks()
  {
    $tasks = $this->model->getAll();
    echo json_encode($tasks);
  }

  public function createTask()
  {
    $input = json_decode(file_get_contents('php://input'), true);
    $this->model->add($input['title'], $input['description']);
    echo json_encode(['message' => 'Task created!']);
  }
}
