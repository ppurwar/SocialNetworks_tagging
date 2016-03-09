/***************************************************************
 *
 * OpenBeacon.org - RGB Strip control - colour correction
 *
 * Copyright 2014 Milosch Meriac <milosch@meriac.com>
 *
 ***************************************************************

 This program is free software; you can redistribute it and/or modify
 it under the terms of the GNU General Public License as published by
 the Free Software Foundation; version 2.

 This program is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 GNU General Public License for more details.

 You should have received a copy of the GNU General Public License along
 with this program; if not, write to the Free Software Foundation, Inc.,
 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

 */
 
#ifndef __CIE1931_H__
#define __CIE1931_H__

#define CIE_MAX_INDEX 128

// CIE1931 colour correction
const uint8_t g_cie[CIE_MAX_INDEX] = {
	0x80, 0x80, 0x80, 0x80, 0x80, 0x81, 0x81, 0x81,
	0x81, 0x81, 0x81, 0x81, 0x81, 0x81, 0x82, 0x82,
	0x82, 0x82, 0x82, 0x82, 0x83, 0x83, 0x83, 0x83,
	0x83, 0x84, 0x84, 0x84, 0x84, 0x85, 0x85, 0x85,
	0x86, 0x86, 0x86, 0x87, 0x87, 0x87, 0x88, 0x88,
	0x89, 0x89, 0x8A, 0x8A, 0x8B, 0x8B, 0x8C, 0x8C,
	0x8D, 0x8D, 0x8E, 0x8E, 0x8F, 0x90, 0x90, 0x91,
	0x92, 0x92, 0x93, 0x94, 0x95, 0x95, 0x96, 0x97,
	0x98, 0x99, 0x9A, 0x9A, 0x9B, 0x9C, 0x9D, 0x9E,
	0x9F, 0xA0, 0xA1, 0xA2, 0xA3, 0xA5, 0xA6, 0xA7,
	0xA8, 0xA9, 0xAB, 0xAC, 0xAD, 0xAE, 0xB0, 0xB1,
	0xB2, 0xB4, 0xB5, 0xB7, 0xB8, 0xBA, 0xBB, 0xBD,
	0xBF, 0xC0, 0xC2, 0xC3, 0xC5, 0xC7, 0xC9, 0xCA,
	0xCC, 0xCE, 0xD0, 0xD2, 0xD4, 0xD6, 0xD8, 0xDA,
	0xDC, 0xDE, 0xE0, 0xE2, 0xE5, 0xE7, 0xE9, 0xEB,
	0xEE, 0xF0, 0xF3, 0xF5, 0xF7, 0xFA, 0xFC, 0xFF,
};

#endif/*__CIE1931_H__*/
