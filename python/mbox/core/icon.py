# -*- coding:utf-8 -*-

# maya
import maya.api.OpenMaya as om
import pymel.core as pm
import pymel.util as pmu
from pymel.core import datatypes

#
import math

# mbox
from mbox.core import curve
from mbox.core import attribute


#############################################
# ICON
#############################################


def create(parent=None,
           name="icon",
           m=datatypes.Matrix(),
           color=[0, 0, 0],
           icon="cube",
           **kwargs):
    """Icon master function
    **Create icon master function.**
    This function centralize all the icons creation
    Arguments:
        parent (dagNode): The parent for the new icon
        name (str): Name of the Icon.
        m (matrix): Transformation matrix of the icon
        color (int or list of float): The color in index base or RGB.
        icon (str): Icon type. Options: "cube", "pyramid", "square",
            "flower", "circle", "cylinder", "compas", "diamond",
                    "cubewithpeak", "sphere", "arrow", "crossarrow",
                    "cross", "null"
        kwargs: The keyword arguments can vary depending of the icon type.
                    Please refear to the specific icon method for more info.
    Returns:
        dagNode: The newly created icon.
    """
    if "w" not in kwargs.keys():
        kwargs["w"] = 1
    if "h" not in kwargs.keys():
        kwargs["h"] = 1
    if "d" not in kwargs.keys():
        kwargs["d"] = 1
    if "po" not in kwargs.keys():
        kwargs["po"] = None
    if "ro" not in kwargs.keys():
        kwargs["ro"] = None
    if "degree" not in kwargs.keys():
        kwargs["degree"] = 3

    if icon == "cube":
        ctl = cube(parent,
                   name,
                   kwargs["w"],
                   kwargs["h"],
                   kwargs["d"],
                   color,
                   m,
                   kwargs["po"],
                   kwargs["ro"])
    elif icon == "pyramid":
        ctl = pyramid(parent,
                      name,
                      kwargs["w"],
                      kwargs["h"],
                      kwargs["d"],
                      color,
                      m,
                      kwargs["po"],
                      kwargs["ro"])
    elif icon == "square":
        ctl = square(parent,
                     name,
                     kwargs["w"],
                     kwargs["d"],
                     color,
                     m,
                     kwargs["po"],
                     kwargs["ro"])
    elif icon == "flower":
        ctl = flower(parent,
                     name,
                     kwargs["w"],
                     color,
                     m,
                     kwargs["po"],
                     kwargs["ro"],
                     kwargs["degree"])
    elif icon == "circle":
        ctl = circle(parent,
                     name,
                     kwargs["w"],
                     color,
                     m,
                     kwargs["po"],
                     kwargs["ro"],
                     kwargs["degree"])
    elif icon == "cylinder":
        ctl = cylinder(parent,
                       name,
                       kwargs["w"],
                       kwargs["h"],
                       color,
                       m,
                       kwargs["po"],
                       kwargs["ro"],
                       kwargs["degree"])
    elif icon == "compas":
        ctl = compas(parent,
                     name,
                     kwargs["w"],
                     color,
                     m,
                     kwargs["po"],
                     kwargs["ro"],
                     kwargs["degree"])
    elif icon == "diamond":
        ctl = diamond(parent,
                      name,
                      kwargs["w"],
                      color,
                      m,
                      kwargs["po"],
                      kwargs["ro"])
    elif icon == "cubewithpeak":
        ctl = cubewithpeak(parent,
                           name,
                           kwargs["w"],
                           color,
                           m,
                           kwargs["po"],
                           kwargs["ro"])
    elif icon == "sphere":
        ctl = sphere(parent,
                     name,
                     kwargs["w"],
                     color,
                     m,
                     kwargs["po"],
                     kwargs["ro"],
                     kwargs["degree"])
    elif icon == "arrow":
        ctl = arrow(parent,
                    name,
                    kwargs["w"],
                    color,
                    m,
                    kwargs["po"],
                    kwargs["ro"])
    elif icon == "crossarrow":
        ctl = crossarrow(parent,
                         name,
                         kwargs["w"],
                         color,
                         m,
                         kwargs["po"],
                         kwargs["ro"])
    elif icon == "cross":
        ctl = cross(parent,
                    name,
                    kwargs["w"],
                    color,
                    m,
                    kwargs["po"],
                    kwargs["ro"])
    elif icon == "null":
        ctl = null(parent,
                   name,
                   kwargs["w"],
                   color,
                   m,
                   kwargs["po"],
                   kwargs["ro"])

    else:
        return

    return ctl


def cube(parent=None,
         name="cube",
         width=1,
         height=1,
         depth=1,
         color=[0, 0, 0],
         m=datatypes.Matrix(),
         pos_offset=None,
         rot_offset=None):
    """Create a curve with a CUBE shape.
    Arguments:
        parent (dagNode): The parent object of the newly created curve.
        name (str): Name of the curve.
        width (float): Width of the shape.
        height (float): Height of the shape.
        depth (float): Depth of the shape.
        color (int or list of float): The color in index base or RGB.
        m (matrix): The global transformation of the curve.
        pos_offset (vector): The xyz position offset of the curve
            from its center.
        rot_offset (vector): The xyz rotation offset of the curve
            from its center. xyz in radians
    Returns:
        dagNode: The newly created icon.
    """
    lenX = width * 0.5
    lenY = height * 0.5
    lenZ = depth * 0.5

    # p is positive, N is negative
    ppp = datatypes.Vector(lenX, lenY, lenZ)
    ppN = datatypes.Vector(lenX, lenY, lenZ * -1)
    pNp = datatypes.Vector(lenX, lenY * -1, lenZ)
    Npp = datatypes.Vector(lenX * -1, lenY, lenZ)
    pNN = datatypes.Vector(lenX, lenY * -1, lenZ * -1)
    NNp = datatypes.Vector(lenX * -1, lenY * -1, lenZ)
    NpN = datatypes.Vector(lenX * -1, lenY, lenZ * -1)
    NNN = datatypes.Vector(lenX * -1, lenY * -1, lenZ * -1)

    v_array = [ppp, ppN, NpN, NNN, NNp, Npp, NpN, Npp, ppp, pNp, NNp, pNp, pNN,
               ppN, pNN, NNN]

    points = get_point_array_with_offset(v_array,
                                         pos_offset,
                                         rot_offset)

    node = curve.add_curve(parent, name, points, False, 1, m)
    curve.set_color(node, color)

    return node


def pyramid(parent=None,
            name="pyramid",
            width=1,
            height=1,
            depth=1,
            color=[0, 0, 0],
            m=datatypes.Matrix(),
            pos_offset=None,
            rot_offset=None):
    """Create a curve with a PYRAMIDE shape.
    Arguments:
        parent (dagNode): The parent object of the newly created curve.
        name (str): Name of the curve.
        width (float): Width of the shape.
        height (float): Height of the shape.
        depth (float): Depth of the shape.
        color (int or list of float): The color in index base or RGB.
        m (matrix): The global transformation of the curve.
        pos_offset (vector): The xyz position offset of the curve
            from its center.
        rot_offset (vector): The xyz rotation offset of the curve
            from its center. xyz in radians
    Returns:
        dagNode: The newly created icon.
    """
    lenX = width * 0.5
    lenY = height
    lenZ = depth * 0.5

    # p is positive, N is negative
    top = datatypes.Vector(0, lenY, 0)
    pp = datatypes.Vector(lenX, 0, lenZ)
    pN = datatypes.Vector(lenX, 0, lenZ * -1)
    Np = datatypes.Vector(lenX * -1, 0, lenZ)
    NN = datatypes.Vector(lenX * -1, 0, lenZ * -1)

    v_array = [pp, top, pN, pp, Np, top, NN, Np, NN, pN]

    points = get_point_array_with_offset(v_array, pos_offset, rot_offset)

    node = curve.addcurve(parent, name, points, False, 1, m)
    curve.set_color(node, color)

    return node


def square(parent=None,
           name="square",
           width=1,
           depth=1,
           color=[0, 0, 0],
           m=datatypes.Matrix(),
           pos_offset=None,
           rot_offset=None):
    """Create a curve with a SQUARE shape.
    Arguments:
        parent (dagNode): The parent object of the newly created curve.
        name (str): Name of the curve.
        width (float): Width of the shape.
        depth (float): Depth of the shape.
        color (int or list of float): The color in index base or RGB.
        m (matrix): The global transformation of the curve.
        pos_offset (vector): The xyz position offset of the curve from
            its center.
        rot_offset (vector): The xyz rotation offset of the curve from
            its center. xyz in radians
    Returns:
        dagNode: The newly created icon.
    """
    lenX = width * 0.5
    lenZ = depth * 0.5

    v0 = datatypes.Vector(lenX, 0, lenZ)
    v1 = datatypes.Vector(lenX, 0, lenZ * -1)
    v2 = datatypes.Vector(lenX * -1, 0, lenZ * -1)
    v3 = datatypes.Vector(lenX * -1, 0, lenZ)

    points = get_point_array_with_offset([v0, v1, v2, v3], pos_offset, rot_offset)

    node = curve.add_curve(parent, name, points, True, 1, m)
    curve.set_color(node, color)

    return node


def flower(parent=None,
           name="flower",
           width=1,
           color=[0, 0, 0],
           m=datatypes.Matrix(),
           pos_offset=None,
           rot_offset=None,
           degree=3):
    """Create a curve with a FLOWER shape.
    Arguments:
        parent (dagNode): The parent object of the newly created curve.
        name (str): Name of the curve.
        width (float): Width of the shape.
        color (int or list of float): The color in index base or RGB.
        m (matrix): The global transformation of the curve.
        pos_offset (vector): The xyz position offset of the curve from
            its center.
        rot_offset (vector): The xyz rotation offset of the curve from
            its center. xyz in radians
    Returns:
        dagNode: The newly created icon.
    """
    dlen = width

    v0 = datatypes.Vector(0, -dlen, 0)
    v1 = datatypes.Vector(-dlen * .4, dlen * .4, 0)
    v2 = datatypes.Vector(dlen, 0, 0)
    v3 = datatypes.Vector(-dlen * .4, -dlen * .4, 0)
    v4 = datatypes.Vector(0, dlen, 0)
    v5 = datatypes.Vector(dlen * .4, -dlen * .4, 0)
    v6 = datatypes.Vector(-dlen, 0, 0)
    v7 = datatypes.Vector(dlen * .4, dlen * .4, 0)

    points = get_point_array_with_offset(
        [v0, v1, v2, v3, v4, v5, v6, v7], pos_offset, rot_offset)

    node = curve.add_curve(parent, name, points, True, degree, m)
    curve.set_color(node, color)

    return node


def circle(parent=None,
           name="circle",
           width=1,
           color=[0, 0, 0],
           m=datatypes.Matrix(),
           pos_offset=None,
           rot_offset=None,
           degree=3):
    """Create a curve with a CIRCLE shape.
    Arguments:
        parent (dagNode): The parent object of the newly created curve.
        name (str): Name of the curve.
        width (float): Width of the shape.
        color (int or list of float): The color in index base or RGB.
        m (matrix): The global transformation of the curve.
        pos_offset (vector): The xyz position offset of the curve from
            its center.
        rot_offset (vector): The xyz rotation offset of the curve from
            its center. xyz in radians
    Returns:
        dagNode: The newly created icon.
    """
    dlen = width * 0.5

    v0 = datatypes.Vector(0, 0, -dlen * 1.108)
    v1 = datatypes.Vector(dlen * .78, 0, -dlen * .78)
    v2 = datatypes.Vector(dlen * 1.108, 0, 0)
    v3 = datatypes.Vector(dlen * .78, 0, dlen * .78)
    v4 = datatypes.Vector(0, 0, dlen * 1.108)
    v5 = datatypes.Vector(-dlen * .78, 0, dlen * .78)
    v6 = datatypes.Vector(-dlen * 1.108, 0, 0)
    v7 = datatypes.Vector(-dlen * .78, 0, -dlen * .78)

    points = get_point_array_with_offset(
        [v0, v1, v2, v3, v4, v5, v6, v7], pos_offset, rot_offset)

    node = curve.add_curve(parent, name, points, True, degree, m)
    curve.set_color(node, color)

    return node


def cylinder(parent=None,
             name="cylinder",
             width=1,
             heigth=1,
             color=[0, 0, 0],
             m=datatypes.Matrix(),
             pos_offset=None,
             rot_offset=None,
             degree=3):
    """Create a curve with a CYLINDER shape.
    Arguments:
        parent (dagNode): The parent object of the newly created curve.
        name (str): Name of the curve.
        width (float): Width of the shape.
        height (float): Height of the shape.
        color (int or list of float): The color in index base or RGB.
        m (matrix): The global transformation of the curve.
        pos_offset (vector): The xyz position offset of the curve from
            its center.
        rot_offset (vector): The xyz rotation offset of the curve from
            its center. xyz in radians
    Returns:
        dagNode: The newly created icon.
    """
    dlen = width * .5
    dhei = heigth * .5

    if degree == 3:
        offsetMult = 1
    else:
        offsetMult = 1.108

    # upper circle
    v0 = datatypes.Vector(0, dhei, -dlen * 1.108)
    v1 = datatypes.Vector(dlen * .78, dhei, -dlen * .78)
    v2 = datatypes.Vector(dlen * 1.108, dhei, 0)
    v3 = datatypes.Vector(dlen * .78, dhei, dlen * .78)
    v4 = datatypes.Vector(0, dhei, dlen * 1.108)
    v5 = datatypes.Vector(-dlen * .78, dhei, dlen * .78)
    v6 = datatypes.Vector(-dlen * 1.108, dhei, 0)
    v7 = datatypes.Vector(-dlen * .78, dhei, -dlen * .78)

    # lower circle
    v8 = datatypes.Vector(0, -dhei, -dlen * 1.108)
    v9 = datatypes.Vector(dlen * .78, -dhei, -dlen * .78)
    v10 = datatypes.Vector(dlen * 1.108, -dhei, 0)
    v11 = datatypes.Vector(dlen * .78, -dhei, dlen * .78)
    v12 = datatypes.Vector(0, -dhei, dlen * 1.108)
    v13 = datatypes.Vector(-dlen * .78, -dhei, dlen * .78)
    v14 = datatypes.Vector(-dlen * 1.108, -dhei, 0)
    v15 = datatypes.Vector(-dlen * .78, -dhei, -dlen * .78)

    # curves
    v16 = datatypes.Vector(0, dhei, -dlen * offsetMult)
    v17 = datatypes.Vector(0, -dhei, -dlen * offsetMult)
    v18 = datatypes.Vector(0, -dhei, dlen * offsetMult)
    v19 = datatypes.Vector(0, dhei, dlen * offsetMult)

    v20 = datatypes.Vector(dlen * offsetMult, dhei, 0)
    v21 = datatypes.Vector(dlen * offsetMult, -dhei, 0)
    v22 = datatypes.Vector(-dlen * offsetMult, - dhei, 0)
    v23 = datatypes.Vector(-dlen * offsetMult, dhei, 0)

    points = get_point_array_with_offset(
        [v0, v1, v2, v3, v4, v5, v6, v7], pos_offset, rot_offset)
    node = curve.add_curve(parent, name, points, True, degree, m)

    points = get_point_array_with_offset(
        [v8, v9, v10, v11, v12, v13, v14, v15], pos_offset, rot_offset)
    crv_0 = curve.add_curve(parent, node + "_0crv", points, True, degree, m)

    points = get_point_array_with_offset([v16, v17], pos_offset, rot_offset)
    crv_1 = curve.add_curve(parent, node + "_1crv", points, True, 1, m)

    points = get_point_array_with_offset([v18, v19], pos_offset, rot_offset)
    crv_2 = curve.add_curve(parent, node + "_2crv", points, True, 1, m)

    points = get_point_array_with_offset([v20, v21], pos_offset, rot_offset)
    crv_3 = curve.add_curve(parent, node + "_3crv", points, True, 1, m)

    points = get_point_array_with_offset([v22, v23], pos_offset, rot_offset)
    crv_4 = curve.add_curve(parent, node + "_4crv", points, True, 1, m)

    for crv in [crv_0, crv_1, crv_2, crv_3, crv_4]:
        for shp in crv.listRelatives(shapes=True):
            node.addChild(shp, add=True, shape=True)
        pm.delete(crv)

    curve.set_color(node, color)

    return node


def compas(parent=None,
           name="compas",
           width=1,
           color=[0, 0, 0],
           m=datatypes.Matrix(),
           pos_offset=None,
           rot_offset=None,
           degree=3):
    """Create a curve with a COMPAS shape.
    Arguments:
        parent (dagNode): The parent object of the newly created curve.
        name (str): Name of the curve.
        width (float): Width of the shape.
        color (int or list of float): The color in index base or RGB.
        m (matrix): The global transformation of the curve.
        pos_offset (vector): The xyz position offset of the curve from
            its center.
        rot_offset (vector): The xyz rotation offset of the curve from
            its center. xyz in radians
    Returns:
        dagNode: The newly created icon.
    """
    dlen = width * 0.5

    division = 24

    point_pos = []
    v = datatypes.Vector(0, 0, dlen)

    for i in range(division):
        if i == division / 2:
            w = datatypes.Vector(v.x, v.y, v.z - dlen * .4)
        else:
            w = datatypes.Vector(v.x, v.y, v.z)
        point_pos.append(w)
        v = v.rotateBy((0, (2 * pmu.math.pi) / (division + 0.0), 0))

    points = get_point_array_with_offset(point_pos, pos_offset, rot_offset)
    node = curve.add_curve(parent, name, points, True, degree, m)
    curve.set_color(node, color)

    return node


def diamond(parent=None,
            name="diamond",
            width=1,
            color=[0, 0, 0],
            m=datatypes.Matrix(),
            pos_offset=None,
            rot_offset=None):
    """Create a curve with a DIAMOND shape.
    Arguments:
        parent (dagNode): The parent object of the newly created curve.
        name (str): Name of the curve.
        width (float): Width of the shape.
        height (float): Height of the shape.
        depth (float): Depth of the shape.
        color (int or list of float): The color in index base or RGB.
        m (matrix): The global transformation of the curve.
        pos_offset (vector): The xyz position offset of the curve from
            its center.
        rot_offset (vector): The xyz rotation offset of the curve from
            its center. xyz in radians
    Returns:
        dagNode: The newly created icon.
    """
    dlen = width * 0.5

    top = datatypes.Vector(0, dlen, 0)
    pp = datatypes.Vector(dlen, 0, dlen)
    pN = datatypes.Vector(dlen, 0, dlen * -1)
    Np = datatypes.Vector(dlen * -1, 0, dlen)
    NN = datatypes.Vector(dlen * -1, 0, dlen * -1)
    bottom = (0, -dlen, 0)

    v_array = [pp, top, pN, pp, Np, top, NN, Np, NN, pN, bottom, NN, bottom,
               Np, bottom, pp]

    points = get_point_array_with_offset(v_array, pos_offset, rot_offset)

    node = curve.add_curve(parent, name, points, False, 1, m)
    curve.set_color(node, color)

    return node


def cubewithpeak(parent=None,
                 name="cubewithpeak",
                 width=1,
                 color=[0, 0, 0],
                 m=datatypes.Matrix(),
                 pos_offset=None,
                 rot_offset=None):
    """Create a curve with a CUBE WITH PEAK shape.
    Arguments:
        parent (dagNode): The parent object of the newly created curve.
        name (str): Name of the curve.
        width (float): Width of the shape.
        color (int or list of float): The color in index base or RGB.
        m (matrix): The global transformation of the curve.
        pos_offset (vector): The xyz position offset of the curve from
            its center.
        rot_offset (vector): The xyz rotation offset of the curve from
            its center. xyz in radians
    Returns:
        dagNode: The newly created icon.
    """
    dlen = width * 0.5

    peak = datatypes.Vector(0, width, 0)
    ppp = datatypes.Vector(dlen, dlen, dlen)
    ppN = datatypes.Vector(dlen, dlen, dlen * -1)
    pNp = datatypes.Vector(dlen, 0, dlen)
    Npp = datatypes.Vector(dlen * -1, dlen, dlen)
    pNN = datatypes.Vector(dlen, 0, dlen * -1)
    NNp = datatypes.Vector(dlen * -1, 0, dlen)
    NpN = datatypes.Vector(dlen * -1, dlen, dlen * -1)
    NNN = datatypes.Vector(dlen * -1, 0, dlen * -1)

    v_array = [peak, ppp, ppN, peak, NpN, ppN, NpN, peak, Npp, NpN, NNN, NNp,
               Npp, NpN, Npp, ppp, pNp, NNp, pNp, pNN, ppN, pNN, NNN]

    points = get_point_array_with_offset(v_array, pos_offset, rot_offset)

    node = curve.add_curve(parent, name, points, False, 1, m)
    curve.set_color(node, color)

    return node


def sphere(parent=None,
           name="sphere",
           width=1,
           color=[0, 0, 0],
           m=datatypes.Matrix(),
           pos_offset=None,
           rot_offset=None,
           degree=3):
    """Create a curve with a SPHERE shape.
    Arguments:
        parent (dagNode): The parent object of the newly created curve.
        name (str): Name of the curve.
        width (float): Width of the shape.
        color (int or list of float): The color in index base or RGB.
        m (matrix): The global transformation of the curve.
        pos_offset (vector): The xyz position offset of the curve from
            its center.
        rot_offset (vector): The xyz rotation offset of the curve from
            its center. xyz in radians
    Returns:
        dagNode: The newly created icon.
    """
    dlen = width * .5

    v0 = datatypes.Vector(0, 0, -dlen * 1.108)
    v1 = datatypes.Vector(dlen * .78, 0, -dlen * .78)
    v2 = datatypes.Vector(dlen * 1.108, 0, 0)
    v3 = datatypes.Vector(dlen * .78, 0, dlen * .78)
    v4 = datatypes.Vector(0, 0, dlen * 1.108)
    v5 = datatypes.Vector(-dlen * .78, 0, dlen * .78)
    v6 = datatypes.Vector(-dlen * 1.108, 0, 0)
    v7 = datatypes.Vector(-dlen * .78, 0, -dlen * .78)

    ro = datatypes.Vector([1.5708, 0, 0])

    points = get_point_array_with_offset(
        [v0, v1, v2, v3, v4, v5, v6, v7], pos_offset, rot_offset)
    node = curve.add_curve(parent, name, points, True, degree, m)

    if rot_offset:
        rot_offset += ro
    else:
        rot_offset = ro
    points = get_point_array_with_offset(
        [v0, v1, v2, v3, v4, v5, v6, v7], pos_offset, rot_offset)
    crv_0 = curve.add_curve(parent, node + "_0crv", points, True, degree, m)

    ro = datatypes.Vector([1.5708, 0, 1.5708])
    if rot_offset:
        rot_offset += ro
    else:
        rot_offset = ro
    points = get_point_array_with_offset(
        [v0, v1, v2, v3, v4, v5, v6, v7], pos_offset, rot_offset + ro + ro)

    crv_1 = curve.add_curve(parent, node + "_1crv", points, True, degree, m)

    for crv in [crv_0, crv_1]:
        for shp in crv.listRelatives(shapes=True):
            node.addChild(shp, add=True, shape=True)
        pm.delete(crv)

    curve.set_color(node, color)

    return node


def arrow(parent=None,
          name="arrow",
          width=1,
          color=[0, 0, 0],
          m=datatypes.Matrix(),
          pos_offset=None,
          rot_offset=None):
    """Create a curve with a ARROW shape.
    Arguments:
        parent (dagNode): The parent object of the newly created curve.
        name (str): Name of the curve.
        width (float): Width of the shape.
        color (int or list of float): The color in index base or RGB.
        m (matrix): The global transformation of the curve.
        pos_offset (vector): The xyz position offset of the curve from
            its center.
        rot_offset (vector): The xyz rotation offset of the curve from
            its center. xyz in radians
    Returns:
        dagNode: The newly created icon.
    """
    dlen = width * 0.5

    v0 = datatypes.Vector(0, 0.3 * dlen, -dlen)
    v1 = datatypes.Vector(0, 0.3 * dlen, 0.3 * dlen)
    v2 = datatypes.Vector(0, 0.6 * dlen, 0.3 * dlen)
    v3 = datatypes.Vector(0, 0, dlen)
    v4 = datatypes.Vector(0, -0.6 * dlen, 0.3 * dlen)
    v5 = datatypes.Vector(0, -0.3 * dlen, 0.3 * dlen)
    v6 = datatypes.Vector(0, -0.3 * dlen, -dlen)

    points = get_point_array_with_offset(
        [v0, v1, v2, v3, v4, v5, v6], pos_offset, rot_offset)

    node = curve.add_curve(parent, name, points, True, 1, m)
    curve.set_color(node, color)

    return node


def crossarrow(parent=None,
               name="crossArrow",
               width=1,
               color=[0, 0, 0],
               m=datatypes.Matrix(),
               pos_offset=None,
               rot_offset=None):
    """Create a curve with a CROSS ARROW shape.
    Arguments:
        parent (dagNode): The parent object of the newly created curve.
        name (str): Name of the curve.
        width (float): Width of the shape.
        color (int or list of float): The color in index base or RGB.
        m (matrix): The global transformation of the curve.
        pos_offset (vector): The xyz position offset of the curve from
            its center.
        rot_offset (vector): The xyz rotation offset of the curve from
            its center. xyz in radians
    Returns:
        dagNode: The newly created icon.
    """
    dlen = width * 0.5

    v0 = datatypes.Vector(0.2 * dlen, 0, 0.2 * dlen)
    v1 = datatypes.Vector(0.2 * dlen, 0, 0.6 * dlen)
    v2 = datatypes.Vector(0.4 * dlen, 0, 0.6 * dlen)
    v3 = datatypes.Vector(0, 0, dlen)
    v4 = datatypes.Vector(-0.4 * dlen, 0, 0.6 * dlen)
    v5 = datatypes.Vector(-0.2 * dlen, 0, 0.6 * dlen)
    v6 = datatypes.Vector(-0.2 * dlen, 0, 0.2 * dlen)
    v7 = datatypes.Vector(-0.6 * dlen, 0, 0.2 * dlen)
    v8 = datatypes.Vector(-0.6 * dlen, 0, 0.4 * dlen)
    v9 = datatypes.Vector(-dlen, 0, 0)
    v10 = datatypes.Vector(-0.6 * dlen, 0, -0.4 * dlen)
    v11 = datatypes.Vector(-0.6 * dlen, 0, -0.2 * dlen)
    v12 = datatypes.Vector(-0.2 * dlen, 0, -0.2 * dlen)
    v13 = datatypes.Vector(-0.2 * dlen, 0, -0.6 * dlen)
    v14 = datatypes.Vector(-0.4 * dlen, 0, -0.6 * dlen)
    v15 = datatypes.Vector(0, 0, -dlen)
    v16 = datatypes.Vector(0.4 * dlen, 0, -0.6 * dlen)
    v17 = datatypes.Vector(0.2 * dlen, 0, -0.6 * dlen)
    v18 = datatypes.Vector(0.2 * dlen, 0, -0.2 * dlen)
    v19 = datatypes.Vector(0.6 * dlen, 0, -0.2 * dlen)
    v20 = datatypes.Vector(0.6 * dlen, 0, -0.4 * dlen)
    v21 = datatypes.Vector(dlen, 0, 0)
    v22 = datatypes.Vector(0.6 * dlen, 0, 0.4 * dlen)
    v23 = datatypes.Vector(0.6 * dlen, 0, 0.2 * dlen)

    v_array = [v0, v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v12, v13, v14,
               v15, v16, v17, v18, v19, v20, v21, v22, v23]
    points = get_point_array_with_offset(v_array, pos_offset, rot_offset)

    node = curve.add_curve(parent, name, points, True, 1, m)
    curve.set_color(node, color)

    return node


def cross(parent=None,
          name="cross",
          width=1,
          color=[0, 0, 0],
          m=datatypes.Matrix(),
          pos_offset=None,
          rot_offset=None):
    """Create a curve with a CROSS shape.
    Arguments:
        parent (dagNode): The parent object of the newly created curve.
        name (str): Name of the curve.
        width (float): Width of the shape.
        color (int or list of float): The color in index base or RGB.
        m (matrix): The global transformation of the curve.
        pos_offset (vector): The xyz position offset of the curve from
            its center.
        rot_offset (vector): The xyz rotation offset of the curve from
            its center. xyz in radians
    Returns:
        dagNode: The newly created icon.
    """
    width = width * 0.35
    offset1 = width * .5
    offset2 = width * 1.5

    v0 = datatypes.Vector(width, offset2, 0)
    v1 = datatypes.Vector(offset2, width, 0)
    v2 = datatypes.Vector(offset1, 0, 0)

    v3 = datatypes.Vector(offset2, -width, 0)
    v4 = datatypes.Vector(width, -offset2, 0)
    v5 = datatypes.Vector(0, -offset1, 0)

    v6 = datatypes.Vector(-width, -offset2, 0)
    v7 = datatypes.Vector(-offset2, -width, 0)
    v8 = datatypes.Vector(-offset1, 0, 0)

    v9 = datatypes.Vector(-offset2, width, 0)
    v10 = datatypes.Vector(-width, offset2, 0)
    v11 = datatypes.Vector(0, offset1, 0)

    points = get_point_array_with_offset(
        [v0, v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11],
        pos_offset,
        rot_offset)

    node = curve.add_curve(parent, name, points, True, 1, m)
    curve.set_color(node, color)

    return node


def null(parent=None,
         name="null",
         width=1,
         color=[0, 0, 0],
         m=datatypes.Matrix(),
         pos_offset=None,
         rot_offset=None):
    """Create a curve with a NULL shape.
    Arguments:
        parent (dagNode): The parent object of the newly created curve.
        name (str): Name of the curve.
        width (float): Width of the shape.
        color (int or list of float): The color in index base or RGB.
        m (matrix): The global transformation of the curve.
        pos_offset (vector): The xyz position offset of the curve from
            its center.
        rot_offset (vector): The xyz rotation offset of the curve from
            its center. xyz in radians
    Returns:
        dagNode: The newly created icon.
    """
    dlen = width * .5

    v0 = datatypes.Vector(dlen, 0, 0)
    v1 = datatypes.Vector(-dlen, 0, 0)
    v2 = datatypes.Vector(0, dlen, 0)
    v3 = datatypes.Vector(0, -dlen, 0)
    v4 = datatypes.Vector(0, 0, dlen)
    v5 = datatypes.Vector(0, 0, -dlen)

    points = get_point_array_with_offset([v0, v1], pos_offset, rot_offset)
    node = curve.add_curve(parent, name, points, False, 1, m)

    points = get_point_array_with_offset([v2, v3], pos_offset, rot_offset)
    crv_0 = curve.add_curve(parent, name, points, False, 1, m)

    points = get_point_array_with_offset([v4, v5], pos_offset, rot_offset)
    crv_1 = curve.add_curve(parent, name, points, False, 1, m)

    for crv in [crv_0, crv_1]:
        for shp in crv.listRelatives(shapes=True):
            node.addChild(shp, add=True, shape=True)
        pm.delete(crv)

    curve.set_color(node, color)

    return node


def axis(parent=None,
         name="axis",
         width=1,
         m=datatypes.Matrix(),
         pos_offset=None,
         rot_offset=None):
    """Create a curve with a AXIS shape.
    Arguments:
        parent (dagNode): The parent object of the newly created curve.
        name (str): Name of the curve.
        width (float): Width of the shape.
        color (int or list of float): The color in index base or RGB.
        m (matrix): The global transformation of the curve.
        pos_offset (vector): The xyz position offset of the curve from
            its center.
        rot_offset (vector): The xyz rotation offset of the curve from
            its center. xyz in radians
    Returns:
        dagNode: The newly created icon.
    """
    dlen = width * .5

    v0 = datatypes.Vector(0, 0, 0)
    v1 = datatypes.Vector(dlen, 0, 0)
    v2 = datatypes.Vector(0, dlen, 0)
    v3 = datatypes.Vector(0, 0, dlen)

    points = get_point_array_with_offset([v0, v1], pos_offset, rot_offset)
    node = curve.add_curve(parent, name, points, False, 1, m)
    curve.set_color(node, 13)

    points = get_point_array_with_offset([v0, v2], pos_offset, rot_offset)
    crv_0 = curve.add_curve(parent, name, points, False, 1, m)
    curve.set_color(crv_0, 14)

    points = get_point_array_with_offset([v0, v3], pos_offset, rot_offset)
    crv_1 = curve.add_curve(parent, name, points, False, 1, m)
    curve.set_color(crv_1, 6)

    for crv in [crv_0, crv_1]:
        for shp in crv.listRelatives(shapes=True):
            node.addChild(shp, add=True, shape=True)
        pm.delete(crv)

    return node


def connection_display_curve(parent, name, centers=list(), degree=1):
    """

    :param parent:
    :param name:
    :param centers:
    :param degree:
    :return:
    """
    crv = curve.add_cns_curve(parent, name, centers, degree)
    crv.attr("overrideEnabled").set(True)
    crv.attr("overrideDisplayType").set(True)

    return crv


def guide_root_icon(parent=None,
                    name="root",
                    width=.5,
                    color=[1, 0, 0],
                    m=datatypes.Matrix(),
                    pos_offset=None,
                    rot_offset=None):
    """Create a curve with a ROOT GUIDE shape.
    Note:
        This icon is specially design for **Shifter** root guides
    Arguments:
        parent (dagNode): The parent object of the newly created curve.
        name (str): Name of the curve.
        width (float): Width of the shape.
        color (int or list of float): The color in index base or RGB.
        m (matrix): The global transformation of the curve.
        pos_offset (vector): The xyz position offset of the curve from
            its center.
        rot_offset (vector): The xyz rotation offset of the curve from
            its center. xyz in radians
    Returns:
        dagNode: The newly created icon.
    """
    rootIco = null(parent, name, width, color, m, pos_offset, rot_offset)
    cubeWidth = width / 2.0
    cubeIco = cube(parent,
                   name,
                   cubeWidth,
                   cubeWidth,
                   cubeWidth,
                   color,
                   m,
                   pos_offset,
                   rot_offset)

    for shp in cubeIco.listRelatives(shapes=True):
        rootIco.addChild(shp, add=True, shape=True)
    pm.delete(cubeIco)

    attribute.non_key(rootIco, attrs=["tx", "ty", "tz",
                                      "rx", "ry", "rz",
                                      "sx", "sy", "sz",
                                      "v"])
    attribute.add(rootIco, "isBlueprintComponent", "bool", keyable=False)
    attribute.lock(rootIco, "v")
    attribute.hide(rootIco, "v")
    # Set the control shapes isHistoricallyInteresting
    for oShape in rootIco.getShapes():
        oShape.isHistoricallyInteresting.set(False)

    return rootIco


def guide_root_icon_2d(parent=None,
                       name="root",
                       width=.5,
                       color=[1, 0, 0],
                       m=datatypes.Matrix(),
                       pos_offset=None,
                       rot_offset=None):
    """Create a curve with a 2D ROOT GUIDE shape.
    Note:
        This icon is specially design for **Shifter** root guides
    Arguments:
        parent (dagNode): The parent object of the newly created curve.
        name (str): Name of the curve.
        width (float): Width of the shape.
        color (int or list of float): The color in index base or RGB.
        m (matrix): The global transformation of the curve.
        pos_offset (vector): The xyz position offset of the curve from
            its center.
        rot_offset (vector): The xyz rotation offset of the curve from
            its center. xyz in radians
    Returns:
        dagNode: The newly created icon.
    """
    rootIco = null(parent, name, width, color, m, pos_offset, rot_offset)
    pm.delete(rootIco.getShapes()[-1])  # Remove the z axis

    rot_offset_orig = datatypes.Vector(math.radians(90), 0, 0)
    if rot_offset:
        rot_offset_orig.rotateBy(rot_offset)

    squareWidth = width / 2.0
    squareIco = square(parent,
                       name,
                       squareWidth,
                       squareWidth,
                       color,
                       m,
                       pos_offset,
                       rot_offset_orig)

    for shp in squareIco.listRelatives(shapes=True):
        rootIco.addChild(shp, add=True, shape=True)
    pm.delete(squareIco)

    attribute.non_key(rootIco, attrs=["tx", "ty", "tz",
                                      "rx", "ry", "rz",
                                      "sx", "sy", "sz",
                                      "v"])
    attribute.add(rootIco, "isGuide", "bool", keyable=False)
    attribute.add(rootIco, "guides", "message", multi=True)
    attribute.lock(rootIco, "v")
    attribute.hide(rootIco, "v")
    # Set the control shapes isHistoricallyInteresting
    for oShape in rootIco.getShapes():
        oShape.isHistoricallyInteresting.set(False)

    return rootIco


def guide_locator_icon(parent=None,
                       name="locator",
                       width=.5,
                       color=[1, 1, 0],
                       m=datatypes.Matrix(),
                       pos_offset=None,
                       rot_offset=None):
    """Create a curve with a LOCATOR GUIDE shape.
    Note:
        This icon is specially design for **Shifter** locator guides
    Arguments:
        parent (dagNode): The parent object of the newly created curve.
        name (str): Name of the curve.
        width (float): Width of the shape.
        color (int or list of float): The color in index base or RGB.
        m (matrix): The global transformation of the curve.
        pos_offset (vector): The xyz position offset of the curve from
            its center.
        rot_offset (vector): The xyz rotation offset of the curve from
            its center. xyz in radians
    Returns:
        dagNode: The newly created icon.
    """
    rootIco = null(parent, name, width, color, m, pos_offset, rot_offset)
    spheWidth = width / 2.0

    sphereIco = sphere(
        parent, name, spheWidth, color, m, pos_offset, rot_offset, degree=3)

    for shp in sphereIco.listRelatives(shapes=True):
        rootIco.addChild(shp, add=True, shape=True)
    pm.delete(sphereIco)

    attribute.non_key(rootIco, attrs=["tx", "ty", "tz",
                                      "rx", "ry", "rz",
                                      "sx", "sy", "sz",
                                      "v"])
    attribute.lock(rootIco, "v")
    attribute.hide(rootIco, "v")
    # Set the control shapes isHistoricallyInteresting
    for oShape in rootIco.getShapes():
        oShape.isHistoricallyInteresting.set(False)

    return rootIco


def guide_blade_icon(parent=None,
                     aim=None,
                     name="blade",
                     lenX=1.0,
                     color=[1, 0, 0],
                     m=datatypes.Matrix(),
                     pos_offset=None,
                     rot_offset=None):
    """

    :param parent:
    :param aim:
    :param name:
    :param lenX:
    :param color:
    :param m:
    :param pos_offset:
    :param rot_offset:
    :return:
    """
    v0 = datatypes.Vector(0, 0, 0)
    v1 = datatypes.Vector(lenX, 0, 0)
    v2 = datatypes.Vector(0, lenX / 3, 0)

    points = get_point_array_with_offset(
        [v0, v1, v2], pos_offset, rot_offset)

    bladeIco = curve.add_curve(parent, name, points, True, 1, m)
    curve.set_color(bladeIco, color)

    attribute.add(bladeIco, "rollOffset", "float", 0)
    attribute.non_key(bladeIco, attrs=["tx", "ty", "tz",
                                       "rx", "ry", "rz",
                                       "sx", "sy", "sz",
                                       "v", "rollOffset"])
    pm.pointConstraint(parent, bladeIco)
    aim_cons = pm.aimConstraint(aim,
                                bladeIco,
                                offset=(0, 0, 0),
                                aimVector=(1, 0, 0),
                                upVector=(0, 1, 0),
                                worldUpType="objectrotation",
                                worldUpVector=(0, 1, 0),
                                worldUpObject=parent)
    bladeIco.rollOffset >> aim_cons.offsetX
    attribute.lock(bladeIco, attrs=["tx", "ty", "tz",
                                    "rx", "ry", "rz",
                                    "sx", "sy", "sz",
                                    "v"])
    attribute.hide(bladeIco, attrs=["tx", "ty", "tz",
                                    "rx", "ry", "rz",
                                    "sx", "sy", "sz",
                                    "v"])
    # bladeIco.scale.set(1, 1, 1)
    # Set the control shapes isHistoricallyInteresting
    for oShape in bladeIco.getShapes():
        oShape.isHistoricallyInteresting.set(False)

    return bladeIco


def get_point_array_with_offset(point_pos, pos_offset=None, rot_offset=None):
    """Get Point array with offset
    Convert a list of vector to a List of float and add the position and
    rotation offset.
    Arguments:
        point_pos (list of vector): Point positions.
        pos_offset (vector):  The position offset of the curve from its
            center.
        rot_offset (vector): The rotation offset of the curve from its
            center. In radians.
    Returns:
        list of vector: the new point positions
    """
    points = list()
    for v in point_pos:
        if rot_offset:
            mv = om.MVector(v.x, v.y, v.z)
            mv = mv.rotateBy(om.MEulerRotation(rot_offset.x,
                                               rot_offset.y,
                                               rot_offset.z,
                                               om.MEulerRotation.kXYZ))
            v = datatypes.Vector(mv.x, mv.y, mv.z)
        if pos_offset:
            v = v + pos_offset

        points.append(v)

    return points
