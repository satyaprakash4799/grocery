import { createSlice, createAsyncThunk } from '@reduxjs/toolkit';
import apiCall from '../../api/axios';


const userAuthenticate = createAsyncThunk('user/authenticateUser', async(data)=> {
    const response = await apiCall('/api/token/','POST',data )
    return response.data;
})

export const userSlicer = createSlice({
    'name': 'user',
    initialState:{
        user: {},
        token: {},
        status:'idle',
        error: null
    },
    reducers: {},
    extraReducers(builder) {
        builder
            .addCase(userAuthenticate.pending, (state) => {
                state.status = 'loading'
            })
            .addCase(userAuthenticate.fulfilled, (state,action) => {
                state.status = 'succeeded'
                state.token.accessToken = action.payload.access;
                state.token.refreshToken = action.payload.refresh;
                localStorage.setItem('accessToken', action.payload.access);
                localStorage.setItem('refreshToken', action.payload.refresh);
            })
            .addCase(userAuthenticate.rejected, (state, action) => {
                state.status = 'rejected';
            })
    }
});



export default userSlicer.reducer;
export {userAuthenticate};