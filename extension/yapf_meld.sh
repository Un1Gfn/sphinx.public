#!/bin/bash

[ -f "$1" ] && meld "$1" <(yapf "$1")
