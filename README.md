# Flask API Panda
A helpful library for Pandas to make their web apis awesome!

## The Problem
Homegrown web API's are often a gross amalgam conflict standards and
usage patterns, and of course, not self documenting.

This library seeks to provide a series of decorator methods that
will provide the following:
    1. Easy ways to add api usage declaration (i.e. self documenting apis)
    2. Easy ways to standardize api responses.

## Usage
  
    from flask.ext import api_panda
    
    @api_panda.add_declaration()
    @api_panda.standardize_response()
    view_method()



