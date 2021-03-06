#ifndef INTERFACE_WORLD_VIEW_GUI_H
#define INTERFACE_WORLD_VIEW_GUI_H

#include "Modeling/World.h"
#include "NavigationGUI.h"
#include <KrisLibrary/math3d/Ray3D.h>
using namespace Math3D;

/** @brief A generic gui with a RobotWorld which allows clicking on entities
 * and loading files.
 *
 * Note: if anything is connected to a ROS topic, OnIdle will call the ROSUpdate() hook
 * and request a redraw.
 * 
 * Accepts commands:
 * - load_file fn: loads a file into the world.
 */
class WorldGUIBackend : public GLNavigationBackend
{
public:
  WorldGUIBackend(RobotWorld* world);
  virtual ~WorldGUIBackend();

  bool LoadCommandLine(int argc,const char** argv);
  bool LoadFile(const char* fn);
  //backend overloads
  virtual void Start();
  virtual bool OnIdle();
  virtual bool OnCommand(const string& cmd,const string& args);
  //GLNavigationBackend overloads
  virtual void SetWorldLights() { world->SetGLLights(); }
  Robot* ClickRobot(int x,int y,int& body,Vector3& localpt) const;
  Robot* ClickRobot(const Ray3D& r,int& body,Vector3& localpt) const;
  RigidObject* ClickObject(int x,int y,Vector3& localpt) const;
  RigidObject* ClickObject(const Ray3D& r,Vector3& localpt) const;
  virtual void RefreshIdle() { SendPauseIdle(0); }
  virtual void RenderWorld();

  virtual void DoFreeDrag(int dx,int dy,int button)
  {
    if(button == 0)  DragRotate(dx,dy);
  }

  virtual void DoCtrlDrag(int dx,int dy,int button)
  {
    if(button == 0)  DragPan(dx,dy);
  }
  
  virtual void DoAltDrag(int dx,int dy,int button)
  {
    if(button == 0)  DragZoom(dx,dy);
  }

  virtual void DoShiftDrag(int dx,int dy,int button)
  {
    if(button == 0) { camera.dist *= (1 + 0.01*Real(dy)); SendRefresh(); }
  }

  virtual bool OnMouseWheel(int dwheel);

  RobotWorld* world;
};



#endif
