//======================================================================
//
// day16.c
// -------
// C implementation of day16. To get the performance needed.
//
//
// (c) 2017 Joachim Strömbergson
//
//======================================================================

#include <stdint.h>
#include <stdlib.h>
#include <stdio.h>

#include "arrays.h"


//------------------------------------------------------------------
// Defines.
//------------------------------------------------------------------
#define spin_cmd 0
#define exchange_cmd 1
#define partner_cmd 2


//------------------------------------------------------------------
// move_t
// The struct used to store all dance moves.
//------------------------------------------------------------------
typedef struct move {
  struct move *next;
  uint8_t cmd;
  uint8_t a;
  uint8_t b;
} move_t;


//------------------------------------------------------------------
// spin()
// i.e. rotate right s steps
//------------------------------------------------------------------
void spin(const uint8_t step, uint8_t *state)
{
  uint8_t tmp;
  for (uint8_t i = 0; i < step; i++) {
    tmp = state[15];
    state[15] = state[14];
    state[14] = state[13];
    state[13] = state[12];
    state[12] = state[11];
    state[11] = state[10];
    state[10] = state[9];
    state[9]  = state[8];
    state[8]  = state[7];
    state[7]  = state[6];
    state[6]  = state[5];
    state[5]  = state[4];
    state[4]  = state[3];
    state[3]  = state[2];
    state[2]  = state[1];
    state[1]  = state[0];
    state[0]  = tmp;
  }
}


//------------------------------------------------------------------
//------------------------------------------------------------------
void exchange(const uint8_t a, const uint8_t b, uint8_t *state)
{
  uint8_t tmp;

  tmp = state[a];
  state[a] = state[b];
  state[b] = tmp;
}


//------------------------------------------------------------------
//------------------------------------------------------------------
uint8_t find_index(const uint8_t a, uint8_t *state)
{
  uint8_t i = 0;
  while (state[i] != a)
    i++;

  return i;
}


//------------------------------------------------------------------
//------------------------------------------------------------------
void partner(const uint8_t a, const uint8_t b, uint8_t *state)
{
  uint8_t ai = find_index(a, state);
  uint8_t bi = find_index(b, state);
  exchange(ai, bi, state);
}


//------------------------------------------------------------------
// dance()
// Perform the given dance on the state by walking through
// all the move structs and performing the different moves.
//------------------------------------------------------------------
void dance(uint8_t *state)
{
  uint8_t cmd, a, b;

  //  printf("Starting to dance...\n");

  for (uint32_t i = 0 ; i < 10000 ; i++) {
    cmd = cmd_array[i];
    a = a_array[i];
    b = b_array[i];
    //    printf("Dance %04d: cmd = %d, a = %03d, b = %03d\n", i, cmd, a, b);

    if (cmd == spin_cmd)
      spin(a, state);

    if (cmd == exchange_cmd)
      exchange(a, b, state);

    if (cmd == partner_cmd)
      partner(a, b, state);

  }
}


//------------------------------------------------------------------
// print_state()
//------------------------------------------------------------------
void print_state(uint8_t *state)
{
  printf("state: ");
  for (uint8_t i = 0; i < 16; i++)
    printf("%c", state[i]);
  printf("\n");
}


//------------------------------------------------------------------
// main()
//------------------------------------------------------------------
int main(void)
{
  uint8_t state[16] = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                       'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p'};

  print_state(&state[0]);
  dance(&state[0]);
  print_state(&state[0]);
  printf("\n");

  printf("Doing the big dance...\n");
  for (uint32_t i = 0 ; i < (1000000000 - 1) ; i++) {
    if (i % 1000000 == 0) {
      printf("%010d\n", i);
    }
    dance(&state[0]);
  }
  printf("Big dance done.\n");
  print_state(&state[0]);

  return 0;
}

//======================================================================
// EOF day16.c
//======================================================================
