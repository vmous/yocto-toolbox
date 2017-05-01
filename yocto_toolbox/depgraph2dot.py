# -*- coding: utf-8 -*-

import argparse
import codecs
from pydot import *
import sys
import re
import traceback
import yaml

def yaml_file_to_pyobj(inf_path):
    '''
    Takes a dependency graph in a YAML file and returns a Python object.

    :param str inf_path: The path to the YAML file
    :returns: A Python object representation of the given dependency graph.
    :raises: YAMLError
    '''
    # Load hflow definition
    pyobj = None
    with codecs.open(inf_path, 'r', 'utf-8') as inf:
        pyobj = yaml.load(inf)

    return pyobj

def json_file_to_pyobj(inf_path):
    psss

def yaml_string_to_pyobj(str):
    '''
    Takes a dependency graph in a YAML string and returns a Python object.

    :param str str: The string representation of the dependency graph in YAML.
    :returns: A Python object representation of the given dependency graph.
    :raises: YAMLError
    '''
    return yaml.load(str)

def normalize_job_name(job_name):
#    print('Before normalization {}'.format(job_name))
#    n = re.sub('%{extract}', '%', job_name)
    n = re.sub('\[\\\\\w\]\.\+', '%{extract}', job_name)
#    print('Before normalization {}'.format(n))
#    print('-----------')
    return n

def pyobj_to_map(pyobj, job_tag='jobs', name_tag='name', dep_tag='dependencies'):
    '''
    Transforms a dependency graph represented as a Python object to a map.

    :param object pyobj: The Python object representation of a dependency graph.
    :param str job_tag: The tag that denotes the jobs section in the dependency graph definition. Default value: \'jobs\'.
    :param str name_tag: The tag that denotes the job name. Default value: \'name\'.
    :param str dep_tag: The tag that denotes the dependencies section in a given job. Default value: \'dependencies\'.
    :returns: A map from job name to list of job names denoting its dependencies.
              key: <job_name>, value: [<other_job_name>*]
    '''
    j2dep = {}
#    j2child = {}

    for job in pyobj[job_tag]:
        job_name = normalize_job_name(job[name_tag])
        try:
            job_deps = job[dep_tag] if job[dep_tag] else []
            for i, dep in enumerate(job_deps):
                job_deps[i] = normalize_job_name(dep)
        except KeyError as ke:
            job_deps = []

        j2dep[job_name] = job_deps

#    for job_name in j2dep.keys():
#        j2child[job_name] = [n for (n, d) in j2dep.items() if job_name in d]

    return j2dep

def map_to_dot(j2dep):
    '''
    Transforms jobs to dependencies mapping to a graph expressed in the DOT (http://www.graphviz.org/content/dot-language) language.

    :param map j2dep: A map from job name to list of job names denoting its dependencies.
    :returns: A DOT graph.
    '''
    graph = Dot(graph_type='digraph')
    for job_name in j2dep.keys():
        graph.add_node(Node(job_name))
    for (job_name, job_deps) in j2dep.items():
        if job_deps != []:
            for dep in job_deps:
                graph.add_edge(Edge(dep, job_name))
    return graph

def dot_to_file(graph, outf_path='resources/graph.png'):
    '''
    Print a DOT graph to an image file.

    :param obj graph: A DOT graph.
    :param str outf_path: The path of the output image file.
    :returns Nothing
    '''
    if graph:
        graph.write_png(outf_path)

#def pretty_print(obj, indent=1):
#    print(json.dumps(obj, indent=1))


def main(args):
    # Prepare argument parser
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', action='store', required='True', help='The dependency graph definition file.')
    parser.add_argument('--type', choices=['yaml', 'json'], action='store', required='True', help='The time of the dependency graph definition file.')

    # Parse arguments
    args = parser.parse_args()

    pyobj = yaml_file_to_pyobj(args.input)
    mapping = pyobj_to_map(pyobj)
    graph = map_to_dot(mapping)
    dot_to_file(graph, '{}.png'.format(args.input))

if __name__ == '__main__':
    try:
        sys.exit(main(sys.argv[1:]))
    except KeyboardInterrupt:
        pass
    except (ValueError, IOError) as e:
        sys.stderr.write('%s: %s' % (type(e).__name__, e))
        print(e)
    except Exception as e: # 2.7
        # print a stack trace for unexpected errors
        sys.stderr.write('Unexpected %s:\n%s' % (type(e).__name__,
                                                 traceback.format_exc()))
        print(e)

    sys.exit(1)
