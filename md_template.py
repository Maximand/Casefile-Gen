template = """
---
layout: case
title: %s
author: %s
lead: %s
status: Open
excerpt: %s
researchers:
%s
cves:
%s
product: %s
versions: %s
recommendation: "%s"
workaround: "%s"
start: %s
end:
timeline:
%s

---

## Summary

%s

## What you can do

%s

## What we are doing

%s

{% include timeline.html %}

## More information

%s

"""
