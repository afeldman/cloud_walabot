#include <iostream>
#include <cassert>

#include <walabot.hpp>

using namespace std;
using namespace Walabot;

Walabot::init(){

  this->walabot_result = Walabot_SetSettingsFolder((char*)"/var/lib/walabot");
  assert(this->walabot_result == WALABOT_SUCCESS);

  this->walabot_result = Walabot_ConnectAny();
  assert(this->walabot_result == WALABOT_SUCCESS);
  this->connected = true;
}

Walabot::Walabot(): walabot_result(WALABOT_ERR_USB_READ_FAILURE),
                    walabot_status(STATUS_DISCONNECTED),
                    connected(false),
                    mtimode(false){
  init();
}

Walabot::~Walabot(){
  this->walabot_result = Walabot_Stop();
  assert(this->walabot_result == WALABOT_SUCCESS);

  if(this->connected){
    this->walabot_result = Walabot_Disconnect();
  }

  this->connected = false;

}

WALABOT_RESULT Walabot::init(){

  WALABOT_RESULT res;
  APP_STATUS appStatus;



  res = Walabot_SetProfile(PROF_SENSOR);
  assert(res == WALABOT_SUCCESS);

  res = Walabot_SetArenaR(rArenaMin, rArenaMax, rArenaRes);
  assert(res == WALABOT_SUCCESS);

  res = Walabot_SetArenaTheta(thetaArenaMin, thetaArenaMax, thetaArenaRes);
  assert(res == WALABOT_SUCCESS);

  res = Walabot_SetArenaPhi(phiArenaMin, phiArenaMax, phiArenaRes);
  assert(res == WALABOT_SUCCESS);

  res = Walabot_SetThreshold(threshold);
  assert(res == WALABOT_SUCCESS);

  res = Walabot_SetDynamicImageFilter(FILTER_TYPE_MTI);
  assert(res == WALABOT_SUCCESS);
  this->mtimode = true;

  res = Walabot_Start();
  assert(res == WALABOT_SUCCESS);

  if(!this->mtimode){
    res = Walabot_StartCalibration();
    assert(res == WALABOT_SUCCESS);
  }

  res = Walabot_GetStatus(&appStatus, &calibrationProcess);
  assert(res == WALABOT_SUCCESS);

  return res;
}
