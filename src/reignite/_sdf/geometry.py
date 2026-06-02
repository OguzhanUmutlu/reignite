### THIS FILE WAS AUTO-GENERATED ###
from __future__ import annotations

from xml.etree import ElementTree as ET

import typing
from ..utils.model import BaseModel
from ..utils.errors import SDFError
from ..utils.version import cmp_version

if typing.TYPE_CHECKING:
    from ..elements.box import Box
    from ..elements.capsule import Capsule
    from ..elements.cone import Cone
    from ..elements.cylinder import Cylinder
    from ..elements.ellipsoid import Ellipsoid
    from ..elements.heightmap import Heightmap
    from ..elements.image import Image
    from ..elements.mesh import Mesh
    from ..elements.plane import Plane
    from ..elements.polyline import Polyline
    from ..elements.sphere import Sphere


# noinspection PyUnusedImports
class Geometry(BaseModel):
    def __init__(
        self,
        sdf_version: str | None = None,
        box: "Box" = None,
        capsule: "Capsule" = None,
        cone: "Cone" = None,
        cylinder: "Cylinder" = None,
        ellipsoid: "Ellipsoid" = None,
        empty: None | None = None,
        heightmap: "Heightmap" = None,
        image: "Image" = None,
        mesh: "Mesh" = None,
        plane: "Plane" = None,
        polyline: "Polyline" = None,
        sphere: "Sphere" = None
    ):
        super().__init__(sdf_version)
        self.box = box
        self.capsule = capsule
        self.cone = cone
        self.cylinder = cylinder
        self.ellipsoid = ellipsoid
        self.empty = empty
        self.heightmap = heightmap
        self.image = image
        self.mesh = mesh
        self.plane = plane
        self.polyline = polyline
        self.sphere = sphere
        if self.box is not None and hasattr(self.box, 'to_version'):
            if getattr(self.box, 'sdfversion', None) is None:
                self.box.sdfversion = self.sdfversion
            elif getattr(self.box, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.box = self.box.to_version(self.sdfversion)
        if self.capsule is not None and hasattr(self.capsule, 'to_version'):
            if getattr(self.capsule, 'sdfversion', None) is None:
                self.capsule.sdfversion = self.sdfversion
            elif getattr(self.capsule, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.capsule = self.capsule.to_version(self.sdfversion)
        if self.cone is not None and hasattr(self.cone, 'to_version'):
            if getattr(self.cone, 'sdfversion', None) is None:
                self.cone.sdfversion = self.sdfversion
            elif getattr(self.cone, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.cone = self.cone.to_version(self.sdfversion)
        if self.cylinder is not None and hasattr(self.cylinder, 'to_version'):
            if getattr(self.cylinder, 'sdfversion', None) is None:
                self.cylinder.sdfversion = self.sdfversion
            elif getattr(self.cylinder, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.cylinder = self.cylinder.to_version(self.sdfversion)
        if self.ellipsoid is not None and hasattr(self.ellipsoid, 'to_version'):
            if getattr(self.ellipsoid, 'sdfversion', None) is None:
                self.ellipsoid.sdfversion = self.sdfversion
            elif getattr(self.ellipsoid, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.ellipsoid = self.ellipsoid.to_version(self.sdfversion)
        if self.heightmap is not None and hasattr(self.heightmap, 'to_version'):
            if getattr(self.heightmap, 'sdfversion', None) is None:
                self.heightmap.sdfversion = self.sdfversion
            elif getattr(self.heightmap, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.heightmap = self.heightmap.to_version(self.sdfversion)
        if self.image is not None and hasattr(self.image, 'to_version'):
            if getattr(self.image, 'sdfversion', None) is None:
                self.image.sdfversion = self.sdfversion
            elif getattr(self.image, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.image = self.image.to_version(self.sdfversion)
        if self.mesh is not None and hasattr(self.mesh, 'to_version'):
            if getattr(self.mesh, 'sdfversion', None) is None:
                self.mesh.sdfversion = self.sdfversion
            elif getattr(self.mesh, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.mesh = self.mesh.to_version(self.sdfversion)
        if self.plane is not None and hasattr(self.plane, 'to_version'):
            if getattr(self.plane, 'sdfversion', None) is None:
                self.plane.sdfversion = self.sdfversion
            elif getattr(self.plane, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.plane = self.plane.to_version(self.sdfversion)
        if self.polyline is not None and hasattr(self.polyline, 'to_version'):
            if getattr(self.polyline, 'sdfversion', None) is None:
                self.polyline.sdfversion = self.sdfversion
            elif getattr(self.polyline, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.polyline = self.polyline.to_version(self.sdfversion)
        if self.sphere is not None and hasattr(self.sphere, 'to_version'):
            if getattr(self.sphere, 'sdfversion', None) is None:
                self.sphere.sdfversion = self.sdfversion
            elif getattr(self.sphere, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.sphere = self.sphere.to_version(self.sdfversion)

    def to_version(self, target_version: str) -> "Geometry":
        from ..elements.box import Box
        from ..elements.capsule import Capsule
        from ..elements.cone import Cone
        from ..elements.cylinder import Cylinder
        from ..elements.ellipsoid import Ellipsoid
        from ..elements.heightmap import Heightmap
        from ..elements.image import Image
        from ..elements.mesh import Mesh
        from ..elements.plane import Plane
        from ..elements.polyline import Polyline
        from ..elements.sphere import Sphere
        if self.capsule is not None and cmp_version(target_version, "1.8") < 0:
            raise ValueError(f"'capsule' is not supported in SDF version {target_version} (added in 1.8)")
        if self.cone is not None and cmp_version(target_version, "1.11") < 0:
            raise ValueError(f"'cone' is not supported in SDF version {target_version} (added in 1.11)")
        if self.ellipsoid is not None and cmp_version(target_version, "1.8") < 0:
            raise ValueError(f"'ellipsoid' is not supported in SDF version {target_version} (added in 1.8)")
        if self.empty is not None and cmp_version(target_version, "1.3") < 0:
            raise ValueError(f"'empty' is not supported in SDF version {target_version} (added in 1.3)")
        if self.polyline is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'polyline' is not supported in SDF version {target_version} (added in 1.5)")
        kwargs: dict = {"sdf_version": target_version, "box": self.box.to_version(target_version) if self.box is not None and hasattr(self.box, "to_version") else self.box, "capsule": self.capsule.to_version(target_version) if self.capsule is not None and hasattr(self.capsule, "to_version") else self.capsule, "cone": self.cone.to_version(target_version) if self.cone is not None and hasattr(self.cone, "to_version") else self.cone, "cylinder": self.cylinder.to_version(target_version) if self.cylinder is not None and hasattr(self.cylinder, "to_version") else self.cylinder, "ellipsoid": self.ellipsoid.to_version(target_version) if self.ellipsoid is not None and hasattr(self.ellipsoid, "to_version") else self.ellipsoid, "empty": self.empty, "heightmap": self.heightmap.to_version(target_version) if self.heightmap is not None and hasattr(self.heightmap, "to_version") else self.heightmap, "image": self.image.to_version(target_version) if self.image is not None and hasattr(self.image, "to_version") else self.image, "mesh": self.mesh.to_version(target_version) if self.mesh is not None and hasattr(self.mesh, "to_version") else self.mesh, "plane": self.plane.to_version(target_version) if self.plane is not None and hasattr(self.plane, "to_version") else self.plane, "polyline": self.polyline.to_version(target_version) if self.polyline is not None and hasattr(self.polyline, "to_version") else self.polyline, "sphere": self.sphere.to_version(target_version) if self.sphere is not None and hasattr(self.sphere, "to_version") else self.sphere}
        return self.__class__(**kwargs)

    def to_sdf(self, version: str | None = None) -> ET.Element:
        from ..elements.box import Box
        from ..elements.capsule import Capsule
        from ..elements.cone import Cone
        from ..elements.cylinder import Cylinder
        from ..elements.ellipsoid import Ellipsoid
        from ..elements.heightmap import Heightmap
        from ..elements.image import Image
        from ..elements.mesh import Mesh
        from ..elements.plane import Plane
        from ..elements.polyline import Polyline
        from ..elements.sphere import Sphere
        if self.sdfversion is None and version is not None:
            self.sdfversion = version
        elif version is not None and version != self.sdfversion:
            return self.to_version(str(version)).to_sdf()
        el = ET.Element("geometry")
        if self.box is not None:
            _child_res = self.box.to_sdf(version)
            if isinstance(_child_res, str):
                _item_el = ET.Element('box')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.capsule is not None:
            _child_res = self.capsule.to_sdf(version)
            if isinstance(_child_res, str):
                _item_el = ET.Element('capsule')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.cone is not None:
            _child_res = self.cone.to_sdf(version)
            if isinstance(_child_res, str):
                _item_el = ET.Element('cone')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.cylinder is not None:
            _child_res = self.cylinder.to_sdf(version)
            if isinstance(_child_res, str):
                _item_el = ET.Element('cylinder')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.ellipsoid is not None:
            _child_res = self.ellipsoid.to_sdf(version)
            if isinstance(_child_res, str):
                _item_el = ET.Element('ellipsoid')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.empty is not None:
            _c_tmp = ET.Element("empty")
            _c_tmp.text = str(self.empty)
            el.append(_c_tmp)
        if self.heightmap is not None:
            _child_res = self.heightmap.to_sdf(version)
            if isinstance(_child_res, str):
                _item_el = ET.Element('heightmap')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.image is not None:
            _child_res = self.image.to_sdf(version)
            if isinstance(_child_res, str):
                _item_el = ET.Element('image')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.mesh is not None:
            _child_res = self.mesh.to_sdf(version)
            if isinstance(_child_res, str):
                _item_el = ET.Element('mesh')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.plane is not None:
            _child_res = self.plane.to_sdf(version)
            if isinstance(_child_res, str):
                _item_el = ET.Element('plane')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.polyline is not None:
            _child_res = self.polyline.to_sdf(version)
            if isinstance(_child_res, str):
                _item_el = ET.Element('polyline')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.sphere is not None:
            _child_res = self.sphere.to_sdf(version)
            if isinstance(_child_res, str):
                _item_el = ET.Element('sphere')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str) -> "Geometry | SDFError":
        from ..elements.box import Box
        from ..elements.capsule import Capsule
        from ..elements.cone import Cone
        from ..elements.cylinder import Cylinder
        from ..elements.ellipsoid import Ellipsoid
        from ..elements.heightmap import Heightmap
        from ..elements.image import Image
        from ..elements.mesh import Mesh
        from ..elements.plane import Plane
        from ..elements.polyline import Polyline
        from ..elements.sphere import Sphere
        _c_box = el.find("box")
        if _c_box is not None:
            _res = Box._from_sdf(_c_box, version)
            if isinstance(_res, SDFError):
                return _res.extend("box")
            _box = _res
        else:
            _box = None
        _c_capsule = el.find("capsule")
        if _c_capsule is not None:
            _res = Capsule._from_sdf(_c_capsule, version)
            if isinstance(_res, SDFError):
                return _res.extend("capsule")
            _capsule = _res
        else:
            _capsule = None
        if _capsule is not None and cmp_version(version, "1.8") < 0:
            return SDFError(f"'capsule' is not supported in SDF version {version} (added in 1.8)")
        _c_cone = el.find("cone")
        if _c_cone is not None:
            _res = Cone._from_sdf(_c_cone, version)
            if isinstance(_res, SDFError):
                return _res.extend("cone")
            _cone = _res
        else:
            _cone = None
        if _cone is not None and cmp_version(version, "1.11") < 0:
            return SDFError(f"'cone' is not supported in SDF version {version} (added in 1.11)")
        _c_cylinder = el.find("cylinder")
        if _c_cylinder is not None:
            _res = Cylinder._from_sdf(_c_cylinder, version)
            if isinstance(_res, SDFError):
                return _res.extend("cylinder")
            _cylinder = _res
        else:
            _cylinder = None
        _c_ellipsoid = el.find("ellipsoid")
        if _c_ellipsoid is not None:
            _res = Ellipsoid._from_sdf(_c_ellipsoid, version)
            if isinstance(_res, SDFError):
                return _res.extend("ellipsoid")
            _ellipsoid = _res
        else:
            _ellipsoid = None
        if _ellipsoid is not None and cmp_version(version, "1.8") < 0:
            return SDFError(f"'ellipsoid' is not supported in SDF version {version} (added in 1.8)")
        _c_tmp = el.find("empty")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else None
            _val = str(_text)
            if isinstance(_val, SDFError):
                return _val.extend("empty")
            _empty = _val
        else:
            _empty = None
        if _empty is not None and cmp_version(version, "1.3") < 0:
            return SDFError(f"'empty' is not supported in SDF version {version} (added in 1.3)")
        _c_heightmap = el.find("heightmap")
        if _c_heightmap is not None:
            _res = Heightmap._from_sdf(_c_heightmap, version)
            if isinstance(_res, SDFError):
                return _res.extend("heightmap")
            _heightmap = _res
        else:
            _heightmap = None
        _c_image = el.find("image")
        if _c_image is not None:
            _res = Image._from_sdf(_c_image, version)
            if isinstance(_res, SDFError):
                return _res.extend("image")
            _image = _res
        else:
            _image = None
        _c_mesh = el.find("mesh")
        if _c_mesh is not None:
            _res = Mesh._from_sdf(_c_mesh, version)
            if isinstance(_res, SDFError):
                return _res.extend("mesh")
            _mesh = _res
        else:
            _mesh = None
        _c_plane = el.find("plane")
        if _c_plane is not None:
            _res = Plane._from_sdf(_c_plane, version)
            if isinstance(_res, SDFError):
                return _res.extend("plane")
            _plane = _res
        else:
            _plane = None
        _c_polyline = el.find("polyline")
        if _c_polyline is not None:
            _res = Polyline._from_sdf(_c_polyline, version)
            if isinstance(_res, SDFError):
                return _res.extend("polyline")
            _polyline = _res
        else:
            _polyline = None
        if _polyline is not None and cmp_version(version, "1.5") < 0:
            return SDFError(f"'polyline' is not supported in SDF version {version} (added in 1.5)")
        _c_sphere = el.find("sphere")
        if _c_sphere is not None:
            _res = Sphere._from_sdf(_c_sphere, version)
            if isinstance(_res, SDFError):
                return _res.extend("sphere")
            _sphere = _res
        else:
            _sphere = None
        return cls(sdf_version=version, box=_box, capsule=_capsule, cone=_cone, cylinder=_cylinder, ellipsoid=_ellipsoid, empty=_empty, heightmap=_heightmap, image=_image, mesh=_mesh, plane=_plane, polyline=_polyline, sphere=_sphere)
