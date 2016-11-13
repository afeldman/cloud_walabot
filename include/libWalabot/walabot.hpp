/*\file walabot.hpp
 *\author Anton Feldmann
 *\version 0.1.0
 *\date 05.09.2016
 */
#pragma once

#include <WalabotAPI.h>

#include <memory>

/*!\brief walabot Namespace
 *\namespace libWalabot
 */
namespace libWalabot{

  class Walabot{
  public:
    Walabot();
    ~Walabot();

    bool start();
    bool stop();
    void connect();
    double calibrate();
  };

}
