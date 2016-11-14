/*\file walabot.hpp
 *\author Anton Feldmann
 *\version 0.1.0
 *\date 05.09.2016
 */
#pragma once

#include <WalabotAPI.h>

/*!\brief walabot Namespace
 *\namespace libWalabot
 */
namespace libWalabot{

  class Walabot{
  public:
    Walabot();
    ~Walabot();

  private:
    WALABOT_RESULT init();
    WALABOT_RESULT shutdown();

  private:
    bool connected;
    bool mtimode;
  };

}
