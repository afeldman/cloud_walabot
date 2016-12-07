#include <iostream>
#include <cassert>

#include <walabot.hpp>

using namespace std;
using namespace libWalabot;

void Walabot::init(){
  double rArenaMin = 5.0;
  double rArenaMax = 40.0;
  double rArenaRes = 4.0;
  double thetaArenaMin = -20.0;
  double thetaArenaMax = 20.0;
  double thetaArenaRes = 3.0;
  double phiArenaMin = -30.0;
  double phiArenaMax = 30.0;
  double phiArenaRes = 3.0;
  double threshold = 8.0;

  // get connection to walabot
  this->walabot_result = Walabot_SetSettingsFolder((char*)"/var/lib/walabot");
  assert(this->walabot_result == WALABOT_SUCCESS);

  this->walabot_result = Walabot_ConnectAny();
  assert(this->walabot_result == WALABOT_SUCCESS);
  this->connected = true;

  //set Profile
  this->walabot_result = Walabot_SetProfile(PROF_SENSOR);
  assert(this->walabot_result == WALABOT_SUCCESS);

  // fov values
 this->walabot_result = Walabot_SetArenaR(rArenaMin, rArenaMax, rArenaRes);
 assert(this->walabot_result == WALABOT_SUCCESS);
 this->walabot_result = Walabot_SetArenaTheta(thetaArenaMin, thetaArenaMax, thetaArenaRes);
 assert(this->walabot_result == WALABOT_SUCCESS);
 this->walabot_result = Walabot_SetArenaPhi(phiArenaMin, phiArenaMax, phiArenaRes);
 assert(this->walabot_result == WALABOT_SUCCESS);

 //walabot threashold
 this->walabot_result = Walabot_SetThreshold(threshold);
 assert(this->walabot_result == WALABOT_SUCCESS);

 // filter
 this->walabot_result = Walabot_SetDynamicImageFilter(FILTER_TYPE_MTI);
 assert(this->walabot_result == WALABOT_SUCCESS);
 this->mtimode = true;

 // start walabot
 this->walabot_result = Walabot_Start();
 assert(this->walabot_result == WALABOT_SUCCESS);

 //walabot calibration
 this->walabot_result = Walabot_StartCalibration();
 assert(this->walabot_result == WALABOT_SUCCESS);

 //appstatus
 this->walabot_result = Walabot_GetStatus(&walabot_status, &calibrationProcess);
 assert(this->walabot_result == WALABOT_SUCCESS);
}

Walabot::Walabot(): walabot_result(WALABOT_ERR_USB_READ_FAILURE),
                    walabot_status(STATUS_DISCONNECTED),
                    calibrationProcess(0.0),
                    connected(false),
                    mtimode(false),
                    m_walabotTargets(){
  this->init();
}

WalabotTarget::WalabotTarget(double x,
                             double y,
                             double z,
                             double ampl): x(x),
                                           y(y),
                                           z(z),
                                           ampl(ampl){};
