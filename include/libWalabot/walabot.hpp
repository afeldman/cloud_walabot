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
    virtual ~Walabot();

  private:
    void init();

  private:
    WALABOT_RESULT walabot_result;
    APP_STATUS walabot_status;

    bool connected;
    bool mtimode;
  };

}
