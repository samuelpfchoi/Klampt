# This file was automatically generated by SWIG (http://www.swig.org).
# Version 2.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.




"""
Python interface to KrisLibrary collision detection routines
"""


from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_collide', [dirname(__file__)])
        except ImportError:
            import _collide
            return _collide
        if fp is not None:
            try:
                _mod = imp.load_module('_collide', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _collide = swig_import_helper()
    del swig_import_helper
else:
    import _collide
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0


class doubleArray(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, doubleArray, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, doubleArray, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _collide.new_doubleArray(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _collide.delete_doubleArray
    __del__ = lambda self : None;
    def __getitem__(self, *args): return _collide.doubleArray___getitem__(self, *args)
    def __setitem__(self, *args): return _collide.doubleArray___setitem__(self, *args)
    def cast(self): return _collide.doubleArray_cast(self)
    __swig_getmethods__["frompointer"] = lambda x: _collide.doubleArray_frompointer
    if _newclass:frompointer = staticmethod(_collide.doubleArray_frompointer)
doubleArray_swigregister = _collide.doubleArray_swigregister
doubleArray_swigregister(doubleArray)

def doubleArray_frompointer(*args):
  return _collide.doubleArray_frompointer(*args)
doubleArray_frompointer = _collide.doubleArray_frompointer

class intArray(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, intArray, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, intArray, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _collide.new_intArray(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _collide.delete_intArray
    __del__ = lambda self : None;
    def __getitem__(self, *args): return _collide.intArray___getitem__(self, *args)
    def __setitem__(self, *args): return _collide.intArray___setitem__(self, *args)
    def cast(self): return _collide.intArray_cast(self)
    __swig_getmethods__["frompointer"] = lambda x: _collide.intArray_frompointer
    if _newclass:frompointer = staticmethod(_collide.intArray_frompointer)
intArray_swigregister = _collide.intArray_swigregister
intArray_swigregister(intArray)

def intArray_frompointer(*args):
  return _collide.intArray_frompointer(*args)
intArray_frompointer = _collide.intArray_frompointer


def newGeom():
  """
    newGeom() -> int

    int newGeom() 
    """
  return _collide.newGeom()

def destroyGeom(*args):
  """
    destroyGeom(int geom)

    void destroyGeom(int geom) 
    """
  return _collide.destroyGeom(*args)

def destroy():
  """
    destroy()

    void destroy()

    destroys internal data structures

    destroys internal data structures 
    """
  return _collide.destroy()

def loadGeom(*args):
  """
    loadGeom(int geom, char const * fn) -> bool

    bool loadGeom(int geom, const char
    *fn)

    Loads a geometry from a file. Sets it to the correct type based on the
    file contents.

    Currently supported file extensions are Trimeshes: .tri, any other
    mesh files that Assimp may support (if Klamp't is built using Assimp
    support).

    Point clouds: .pcd

    Primitive geometries: .geom

    Returns False if there is a load error. Raises an exception if the ID
    is invalid. 
    """
  return _collide.loadGeom(*args)

def makeTriMeshGeom(*args):
  """
    makeTriMeshGeom(int geom, char const * fn)
    makeTriMeshGeom(int geom, double const * verts, int const * inds, int nv, int nt)

    void makeTriMeshGeom(int
    geom, const double *verts, const int *inds, int nv, int nt)

    Makes a geometry into a trimesh given the vertex and index data. verts
    is of length nv*3, and inds is of length nt*3.

    Note: in Python, must use doubleArray and intArray for the verts and
    inds objects. 
    """
  return _collide.makeTriMeshGeom(*args)

def setTriMeshTranslation(*args):
  """
    setTriMeshTranslation(int geom, double const [3] t)

    void
    setTriMeshTranslation(int geom, const double t[3])

    Sets the translation of a trimesh geom. 
    """
  return _collide.setTriMeshTranslation(*args)

def setTriMeshRotation(*args):
  """
    setTriMeshRotation(int geom, double const [9] r)

    void
    setTriMeshRotation(int geom, const double r[9])

    Sets the rotation of a trimesh geom. 
    """
  return _collide.setTriMeshRotation(*args)

def getTriMeshTranslation(*args):
  """
    getTriMeshTranslation(int geom)

    void
    getTriMeshTranslation(int geom, double out[3])

    Gets the translation of a trimesh geom. 
    """
  return _collide.getTriMeshTranslation(*args)

def getTriMeshRotation(*args):
  """
    getTriMeshRotation(int geom)

    void
    getTriMeshRotation(int geom, double out[9])

    Gets the rotation of a trimesh geom. 
    """
  return _collide.getTriMeshRotation(*args)

def getTriMeshBB(*args):
  """
    getTriMeshBB(int geom)

    void getTriMeshBB(int geom,
    double out[3], double out2[3])

    Gets the bounding box of a trimesh geom. 
    """
  return _collide.getTriMeshBB(*args)

def getTriMeshNumVerts(*args):
  """
    getTriMeshNumVerts(int geom) -> int

    int getTriMeshNumVerts(int
    geom)

    Gets the number of vertices of a trimesh geom. 
    """
  return _collide.getTriMeshNumVerts(*args)

def getTriMeshNumTris(*args):
  """
    getTriMeshNumTris(int geom) -> int

    int getTriMeshNumTris(int
    geom)

    Gets the number of triangles of a trimesh geom. 
    """
  return _collide.getTriMeshNumTris(*args)

def getTriMeshVerts(*args):
  """
    getTriMeshVerts(int geom) -> double *

    double* getTriMeshVerts(int
    geom)

    Gets the vertex data of a trimesh geom (length nv*3). 
    """
  return _collide.getTriMeshVerts(*args)

def getTriMeshTris(*args):
  """
    getTriMeshTris(int geom) -> int *

    int* getTriMeshTris(int geom)

    Gets the index data of a trimesh geom (length nt*3). 
    """
  return _collide.getTriMeshTris(*args)

def makePointGeom(*args):
  """
    makePointGeom(int geom, double const [3] x)

    void makePointGeom(int geom,
    const double x[3])

    Makes a geom into a point x. 
    """
  return _collide.makePointGeom(*args)

def makeSphereGeom(*args):
  """
    makeSphereGeom(int geom, double const [3] c, double r)

    void makeSphereGeom(int geom,
    const double c[3], double r)

    Makes a geom into a sphere centered at c with radius r. 
    """
  return _collide.makeSphereGeom(*args)

def makeRayGeom(*args):
  """
    makeRayGeom(int geom, double const [3] s, double const [3] d)

    void makeRayGeom(int geom, const
    double s[3], const double d[3])

    Makes a geom into a ray with source s and direction d. 
    """
  return _collide.makeRayGeom(*args)

def makeLineGeom(*args):
  """
    makeLineGeom(int geom, double const [3] s, double const [3] d)

    void makeLineGeom(int geom,
    const double s[3], const double d[3])

    Makes a geom into a line with source s and direction d. 
    """
  return _collide.makeLineGeom(*args)

def makeSegmentGeom(*args):
  """
    makeSegmentGeom(int geom, double const [3] a, double const [3] b)

    void makeSegmentGeom(int
    geom, const double a[3], const double b[3])

    Makes a geom into a segment with endpoints a, b. 
    """
  return _collide.makeSegmentGeom(*args)

def makeAABBGeom(*args):
  """
    makeAABBGeom(int geom, double const [3] bmin, double const [3] bmax)

    void makeAABBGeom(int geom,
    const double bmin[3], const double bmax[3])

    Makes a geom into an axis-aligned bounding box with lower bound bmin
    and upper bound bmax. 
    """
  return _collide.makeAABBGeom(*args)

def makeGroupGeom(*args):
  """
    makeGroupGeom(int geom, int * geoms, int numgeoms)

    void makeGroupGeom(int geom,
    int *geoms, int numgeoms)

    Makes a geom into a group geom from an array of other geoms. Note: in
    Python, must use an intArray for geoms argument. 
    """
  return _collide.makeGroupGeom(*args)

def collide(*args):
  """
    collide(int geom1, int geom2) -> bool

    bool collide(int geom1, int geom2)

    Tests whether the two geometries collide. 
    """
  return _collide.collide(*args)

def withinTolerance(*args):
  """
    withinTolerance(int geom1, int geom2, double tol) -> bool

    bool withinTolerance(int
    geom1, int geom2, double tol)

    Tests whether the two geometries are within the given tolerance. 
    """
  return _collide.withinTolerance(*args)

def distance(*args):
  """
    distance(int geom1, int geom2, double relErr, double absErr) -> double

    double distance(int geom1, int
    geom2, double relErr, double absErr)

    Returns the distance between the two geometries, possibly with an
    approximation error (useful to speed up mesh-mesh distance detection)

    Error of result is no more than D*relErr+absErr where D is the actual
    distance. Set relErr=absErr=0 to get exact distance.

    NOTE: Not yet implemented. 
    """
  return _collide.distance(*args)

def closestPoints(*args):
  """
    closestPoints(int geom1, int geom2)

    void closestPoints(int geom1,
    int geom2, double out[3], double out2[3])

    Returns the closest points between the two geometries. These are given
    in world coordinates.

    NOTE: Not yet implemented. 
    """
  return _collide.closestPoints(*args)

def rayCast(*args):
  """
    rayCast(int geom, double const [3] s, double const [3] d) -> bool

    bool rayCast(int geom, const double
    s[3], const double d[3], double out[3])

    Returns true if the geometry is hit by the given ray, and also returns
    the hit point (in world coordinates). 
    """
  return _collide.rayCast(*args)

def makeCollQuery(*args):
  """
    makeCollQuery(int geom1, int geom2) -> int

    int makeCollQuery(int geom1,
    int geom2)

    Creates a collision query object attachd to the two given geometries.
    For mesh-mesh collisions, on repeated calls, this may be somewhat
    faster than querying from scratch. 
    """
  return _collide.makeCollQuery(*args)

def destroyCollQuery(*args):
  """
    destroyCollQuery(int query)

    void destroyCollQuery(int
    query)

    Deletes a collision query object. 
    """
  return _collide.destroyCollQuery(*args)

def queryCollide(*args):
  """
    queryCollide(int query) -> bool

    bool queryCollide(int query)

    Checks if the two geoms associated with this query are colliding. 
    """
  return _collide.queryCollide(*args)

def queryWithinTolerance(*args):
  """
    queryWithinTolerance(int query, double tol) -> bool

    bool
    queryWithinTolerance(int query, double tol)

    Checks if the two geoms associated with this query are within the
    given tolerance.

    See:   withinTolerance 
    """
  return _collide.queryWithinTolerance(*args)

def queryDistance(*args):
  """
    queryDistance(int query, double relErr, double absErr) -> double

    double queryDistance(int query,
    double relErr, double absErr)

    Computes the distance betweeen the two geoms associated with this
    query.

    See:   distance 
    """
  return _collide.queryDistance(*args)

def queryClosestPoints(*args):
  """
    queryClosestPoints(int query)

    void
    queryClosestPoints(int query, double out[3], double out2[3])

    Computes points that give rise to the closest distance betweeen the
    two geoms associated with this query.

    See:   closestPoints 
    """
  return _collide.queryClosestPoints(*args)

def queryTolerancePoints(*args):
  """
    queryTolerancePoints(int query)

    void
    queryTolerancePoints(int query, double out[3], double out2[3])

    If the two geoms associated with this query are within a given
    tolerance (from a previous queryWithinTolerance call), this produces
    the points on geom1 and geom2, respectively that are within that
    tolerance. 
    """
  return _collide.queryTolerancePoints(*args)
# This file is compatible with both classic and new-style classes.


