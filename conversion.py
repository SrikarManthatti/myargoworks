import pandas as pd
import os
import re

def read_airflow_workflow(path):
    print(os.path.join(path,'workflow.py'))
    with open(os.path.join(path,'workflow.py'), 'r') as f:
        workflow_contents = f.read()
    return workflow_contents

def extract_task_dependancies_lines(wf_content):
    graph_lines  = []
    for line in wf_content.split('\n'):
        if '>>' in line or '<<' in line:
            graph_lines.append([line.strip()])
        #graph_lines.append(each_line)
    return graph_lines

def extract_tasks_from_graph_lines(graph_lines):
    graph_dict = {}
    for tls in graph_lines:
        tasks = "".join(tls).split('>>')
        if tasks[0] not in graph_dict.keys():
            graph_dict[tasks[0]] = tasks[1:]
        else:
            graph_dict[tasks[0]] = graph_dict[tasks[0]]+tasks[1:]
    return graph_dict

def main():
    folder_path = 'example_dags'
    content = read_airflow_workflow(folder_path)
    print(len(content.split('\n')))
    task_lines = extract_task_dependancies_lines(content)
    graph_dictionary = extract_tasks_from_graph_lines(task_lines)
    print(graph_dictionary.keys())
if __name__=="__main__":
    main()

