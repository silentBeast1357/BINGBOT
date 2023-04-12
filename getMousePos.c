#include <stdio.h>
#include <Windows.h>

int main(void)
{
    printf("Press K to get the position of your mouse\n");
    while (1)
    {
        if (GetKeyState('K') & 0x8000)
        {
            POINT cursorPos;
            GetCursorPos(&cursorPos);

            printf("x:%d\ny:%d\n\n",cursorPos.x,cursorPos.y);

            while (GetKeyState('K') & 0x8000)
                continue;
        }
    }
}