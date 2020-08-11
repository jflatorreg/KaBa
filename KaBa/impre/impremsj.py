#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 10:21:20 2020

@author: juanfe
"""


def Imprimir_Mensaje(msj):
    """
    Imprime un mensaje.
    
    :param msj: (str) Variable con el mensaje.
    :return: None 
    """
    print(msj)
    return None


def Imprimir_Mensaje_2(msj):
    """
    Imprime un mensaje
    
    :param msj: (str) Variable con el mensaje.
    :return msjcomple: (str) Variable con el mensaje completo 
    """
    
    print('El mensaje es:',msj)
    msjcomple = 'El mensaje es: ' + msj
    return msjcomple

