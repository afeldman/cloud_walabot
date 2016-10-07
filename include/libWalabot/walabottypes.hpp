/*\file walabot.hpp
 *\author Anton Feldmann
 *\version 0.1.0
 *\date 07.10.2016
 */
#pragma once

#include <cstdint>
#include <WalabotAPI.h>

#define CHECK_WALABOT_RESULT(result, func_name)                       \
  {                                                                   \
    if (result != WALABOT_SUCCESS){                                   \
      uint32_t extended = (uint32_t)Walabot_GetExtendedError();       \
      const uint8_t* errorStr = (uint8_t)Walabot_GetErrorString();    \
      std::cout << std::endl << "Error at " __FILE__ << ":"           \
      << std::dec << __LINE__ << " - "                                \
      << func_name << " result is 0x" << std::hex                     \
      << result << std::endl;                                         \
                                                                      \
      std::cout << "Error string: " << errorStr << std::endl;         \
                                                                      \
      std::cout << "Extended error: 0x" << std::hex                   \
      << extended << std::endl << std::endl;                          \
                                                                      \
      std::cout << "Press enter to continue ...";                     \
      std::string dummy;                                              \
      std::getline(std::cin, dummy);                                  \
      return;                                                         \
    }                                                                 \
  }
