from __future__ import annotations

from pathlib import Path

from reignite import read_sdf, read_sdf_string


def test_read_sdf_string_model():
    xml = """<?xml version="1.0"?>
<sdf version="1.9">
  <model name="demo" static="false">
    <link name="base_link"/>
  </model>
</sdf>
"""
    model = read_sdf_string(xml)
    assert type(model).__name__ == "Model"
    assert getattr(model, "name") == "demo"


def test_read_sdf_file_model():
    fixture = Path(__file__).parent / "fixtures" / "model.sdf"
    model = read_sdf(fixture)
    assert type(model).__name__ == "Model"
    assert getattr(model, "name") == "demo"
