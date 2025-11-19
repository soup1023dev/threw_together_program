#include <stdio.h>
int main(void){
  printf("hello world\n")
  return 0
}

#include <efi.h>
#include <efilib.h>

EFI_STATUS efi_main(EFI_HANDLE img, EFI_SYSTEM_TABLE *systab) {
    InitializeLib(img, systab);
    uefi_call_wrapper(systab->ConOut->OutputString, 2, systab->ConOut, L"Hello World!\n\r");
    return EFI_SUCCESS;
}
# 多分これ動きません、特殊すぎて
