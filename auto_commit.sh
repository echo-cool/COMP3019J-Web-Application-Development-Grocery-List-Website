#!/bin/bash
echo "Enter commit message:\n"
git add .
git commit -m "$0"
git push
echo "push finished!\n"
