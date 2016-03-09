/***************************************************************
 *
 * OpenBeacon.org - FLASH storage support
 *
 * Copyright 2010 Milosch Meriac <meriac@openbeacon.de>
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

#ifndef __STORAGE_H__
#define __STORAGE_H__

#include "msd.h"

#define LOGFILE_STORAGE_SIZE (32*1024*1024)

extern void storage_init (uint16_t device_id, uint8_t connect);
extern void storage_connect (uint8_t enabled_db);
extern void storage_read (uint32_t offset, uint32_t length, void *dst);
extern void storage_write (uint32_t offset, uint32_t length, const void *src);
extern void storage_erase (void);
extern void storage_status (void);

extern int storage_db_find (uint8_t type, uint16_t id);
extern int storage_db_read (void* buffer, uint32_t size);

#endif/*__STORAGE_H__*/
