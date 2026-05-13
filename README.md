# reignite

**Modern Procedural Generation for Gazebo**

`reignite` is a Python library designed to effortlessly generate, manipulate, and read Simulation Description Format (SDFormat / SDF) files, primarily used by the [Gazebo](https://gazebosim.org/) robotics simulator. It provides a highly intuitive and Pythonic object-oriented API to build complex simulated worlds, models, plugins, and sensors, bypassing the need to write verbose XML manually.

## Features

- **Procedural Generation**: Create and configure worlds, models, and plugins using Python code.
- **SDF Parsing**: Parse existing SDF XML files and map them back to native Python objects for manipulation.
- **Strongly Typed Elements**: Make use of structured classes for physics, materials, geometry, lighting, sensors, etc.
- **Version Support**: Export elements to specific SDFormat versions.

## Installation

You can install `reignite` locally or via pip:

```bash
pip install reignite
```

## Usage

### Reading an SDF File

Parse an SDF XML file and instantiate the correct versioned model:

```python
from reignite import read_sdf

world = read_sdf("path/to/world.sdf")
```

### Procedural Generation (Writing an SDF File)

Here is a comprehensive example demonstrating how to procedurally create a simulated world equipped with physics, GUI/server plugins, lighting, spherical coordinates, and primitive models.

```python
from reignite import element_to_root
from reignite.elements import World, Physics, Gui, Scene, Light, Model, Link, Visual
from reignite.elements.geometry import BoxGeometry
from reignite.elements.material import SimpleMaterial
from reignite.elements.plugins import (
    InteractiveViewControlPlugin, MinimalScenePlugin, PhysicsPlugin,
    UserCommandsPlugin, SceneBroadcasterPlugin, ImuPlugin, NavSatPlugin, 
    SensorsPlugin, EntityContextMenuPlugin, GzSceneManagerPlugin, 
    CameraTrackingPlugin, WorldControlPlugin, ComponentInspectorPlugin, EntityTreePlugin
)
from reignite.sdf import SphericalCoordinates
from reignite.utils import Color, Vector3, Pose

# 1. Initialize the World
world = World(name="example_world")

# 2. Configure Physics parameters
world.physics = Physics(
    max_step_size=0.001,
    real_time_factor=1.0,
    real_time_update_rate=1000, 
    ode=Physics.Ode(
        solver=Physics.Ode.OdeSolver(type="quick", iters=50, sor=1.3),
        constraints=Physics.Ode.OdeConstraints(cfm=0.0, erp=0.2)
    )
)

# 3. Add necessary Server Plugins
world.add_plugin(
    PhysicsPlugin(), UserCommandsPlugin(), SceneBroadcasterPlugin(), 
    ImuPlugin(), NavSatPlugin(), SensorsPlugin()
)

world.wind = World.Wind(linear_velocity=Vector3(0.0, 0.0, 0.0))

# 4. Configure the GUI and its Plugins
world.gui = Gui()
world.gui.add_plugin(
    MinimalScenePlugin(), EntityContextMenuPlugin(), GzSceneManagerPlugin(),
    InteractiveViewControlPlugin(), CameraTrackingPlugin(), WorldControlPlugin(),
    ComponentInspectorPlugin(), EntityTreePlugin()
)

# 5. Set up Scene properties
world.scene = Scene(
    ambient=Scene.Ambient(ambient=Color(1.0, 1.0, 1.0)),
    background=Scene.Background(rgba=Color(0.8, 0.8, 0.8)),
    sky=Scene.SceneSky()
)

# 6. Set Environment Spherical Coordinates
world.spherical_coordinates = SphericalCoordinates(
    latitude_deg=47.6062,
    longitude_deg=-122.3321,
    elevation=100.0
)

# 7. Add Lighting
sun = Light(
    type="directional",
    name="sun",
    cast_shadows=True,
    pose=Pose(0.0, 0.0, 10.0),
    diffuse=Light.Diffuse(diffuse=Color(0.8, 0.8, 0.8, 1.0)),
    specular=Light.Specular(specular=Color(0.8, 0.8, 0.8, 1.0)),
    attenuation=Light.Attenuation(range=1000.0, constant=0.9, linear=0.01, quadratic=0.001),
    direction=Light.Direction(direction=Vector3(-0.5, 0.1, -0.9))
)
world.add_light(sun)

# 8. Create and Add Models (e.g., an RGB axes model)
axes = Model(static=True, links=[
    Link(visuals=[
        Visual(
            name="r",
            cast_shadows=False,
            pose=Pose(5.0, 0.0, 0.1),
            geometry=BoxGeometry(Vector3(10.0, 0.01, 0.01)),
            material=SimpleMaterial(Color("#ff0000"))
        ),
        Visual(
            name="g",
            cast_shadows=False,
            pose=Pose(5.0, 0.1, 0.0),
            geometry=BoxGeometry(Vector3(0.01, 10.0, 0.01)),
            material=SimpleMaterial(Color("#00ff00"))
        ),
        Visual(
            name="b",
            cast_shadows=False,
            pose=Pose(0.0, 5.1, 0.0),
            geometry=BoxGeometry(Vector3(0.01, 0.01, 10.0)),
            material=SimpleMaterial(Color("#0000ff"))
        )
    ])
])
world.add_model(axes)

# 9. Export to SDF
element_to_root(world, "1.10").write("world.sdf", encoding="utf-8", xml_declaration=True)
```

## Contributing

Contributions are welcome! Tests are managed via `pytest`.

```bash
pip install -e .[test]
pytest
```

## License

This project is licensed under the MIT License.
