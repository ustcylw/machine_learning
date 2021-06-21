#! /usr/bin/env python
# coding: utf-8
import os, sys
import numpy



class Dijkstra(object):
    def __init__(self, node_map) -> None:
        super().__init__()
        self.start_node = 0
        self.end_node = 0
        self.node_map = node_map
    
    def step(self):
        pass
    
    def __call__(self, start_node, end_node) -> Any:
        self.start_node = start_node
        self.end_node = end_node
        
        if self.start_node == self.end_node:
            pass
            # TODO
        
        