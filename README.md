# reignite

Modern Procedural Generation for Gazebo

## SDF Reader

Parse an SDF XML file and instantiate the correct versioned model:

```python
from reignite import read_sdf

world = read_sdf("path/to/world.sdf")
```
