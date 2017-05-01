import pytest

import pydot
from networkx.drawing import nx_pydot
from networkx.algorithms.isomorphism import isomorph

from yocto_toolbox.depgraph2dot import *

yaml_string = '''namespace: 'foo'
substitutions: 'bar'
jobs:
- name: job_1
  dependencies:
- name: job_2
  dependencies:
    - job_1
- name: job_3
  dependencies:
    - job_1
- name: job_4
  dependencies:
    - job_3
- name: job_5
  dependencies:
    - job_3
- name: job_6
  dependencies:
    - job_4
    - job_5
- name: job_7
  dependencies:
    - job_2
    - job_6
- name: job_8
  dependencies:
    - job_7
- name: job_9
'''

dot_string = '''digraph G {
job_7;
job_5;
job_9;
job_2;
job_1;
job_8;
job_6;
job_4;
job_3;
job_2 -> job_7;
job_6 -> job_7;
job_3 -> job_5;
job_1 -> job_2;
job_7 -> job_8;
job_4 -> job_6;
job_5 -> job_6;
job_3 -> job_4;
job_1 -> job_3;
}
'''

_b = {'namespace': 'foo', 'jobs': [{'name': 'job_1', 'dependencies': None}, {'name': 'job_2', 'dependencies': ['job_1']}, {'name': 'job_3', 'dependencies': ['job_1']}, {'name': 'job_4', 'dependencies': ['job_3']}, {'name':  'job_5', 'dependencies': ['job_3']}, {'name': 'job_6', 'dependencies': ['job_4', 'job_5']}, {'name': 'job_7', 'dependencies': ['job_2', 'job_6']}, {'name': 'job_8', 'dependencies': ['job_7']}, {'name': 'job_9'}], 'substitutions': 'bar'}

def test_yaml_file_to_pyobj():
    a = yaml_file_to_pyobj('resources/test-dep-graph.yaml')
    assert a == _b

def test_yaml_string_to_pyobj():
    a = yaml_string_to_pyobj(yaml_string)

    assert a == _b

def test_pobj_to_map():
    y = yaml_file_to_pyobj('resources/test-dep-graph.yaml')
    j2dep = pyobj_to_map(y)
    
    assert j2dep == {'job_2': ['job_1'], 'job_6': ['job_4', 'job_5'], 'job_1': [], 'job_3': ['job_1'], 'job_9': [], 'job_7': ['job_2', 'job_6'], 'job_5': ['job_3'], 'job_8': ['job_7'], 'job_4': ['job_3']}

def test_map_to_dot():
    _graph = pydot.Dot(graph_type='digraph')
    for i in range(1, 10):
        _graph.add_node(pydot.Node('job_{}'.format(i)))

    _graph.add_edge(pydot.Edge('job_1', 'job_2'))
    _graph.add_edge(pydot.Edge('job_1', 'job_3'))
    _graph.add_edge(pydot.Edge('job_3', 'job_4'))
    _graph.add_edge(pydot.Edge('job_3', 'job_5'))
    _graph.add_edge(pydot.Edge('job_4', 'job_6'))
    _graph.add_edge(pydot.Edge('job_5', 'job_6'))
    _graph.add_edge(pydot.Edge('job_2', 'job_7'))
    _graph.add_edge(pydot.Edge('job_6', 'job_7'))
    _graph.add_edge(pydot.Edge('job_7', 'job_8'))
    
    y = yaml_file_to_pyobj('resources/test-dep-graph.yaml')
    j2dep = pyobj_to_map(y)
    graph = map_to_dot(j2dep)

    nxg = nx_pydot.from_pydot(graph)
    _nxg = nx_pydot.from_pydot(_graph)

    assert isomorph.is_isomorphic(nxg, _nxg)
    #assert 1 == 2

def test_dot_to_file():
    pass
