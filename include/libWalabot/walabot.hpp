/*\file walabot.hpp
 *\author Anton Feldmann
 *\version 0.1.0
 *\date 05.09.2016
 */
#pragma once

#include <memory>
#include <WalabotAPI.h>

#include "walabottypes"

/*!\brief walabot Namespace
 *\namespace libWalabot
 */
namespace libWalabot{

  class Walabot{
  public:
    Walabot();
    ~Walabot();

    boolean start();
    boolean stop();
    void connect();
    double calibrate();
  private:
    shared_memory<SensorTarget> m_sensortarget;
  };

}
